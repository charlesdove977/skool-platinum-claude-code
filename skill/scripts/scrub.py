"""Replace community members' identities in rendered Platinum community files with stable pseudonyms.

usage: python3 -I scrub.py <posts_json_dir> <community_md_dir> [extra .md files ...] [--redact "string" ...]

- Reads every post tree JSON in <posts_json_dir> (written by posts.py + comments.py) to build the roster of authors.
- Skool staff and the program's public mentors keep their names (they speak in an official capacity).
- Every other member becomes "Member xxxx" (4 hex chars from a hash of their Skool user id, so the same
  person gets the same pseudonym on every refresh).
- Removes member profile ids, @mentions, Skool handles, emails, phone numbers and links that are not on the
  allowlist (member websites, socials and their own Skool groups), and drops post images (member screenshots).
- Rewrites files in place and prints the staff list plus a count of replacements. Run leak_check.py after.
"""
import glob, hashlib, json, os, re, sys

KEEP_NAMES = {  # public figures: program host, Skool staff, the interviewed mentors
    "Alex Hormozi", "Mark Novikov", "Sam Ovens", "Nick Saraev", "Oscar Patel", "Josh Madakor", "James Lu",
}
STAFF_BIO = re.compile(r"(@\s*Skool\b|\bat Skool\b|Skool team|Cofounder, Skool|Skool (Creator|Community) (Success|Support))", re.I)
ALLOWED_URL = re.compile(
    r"https?://(www\.)?(skool\.com/(platinum-october|skoolers|blog|pricing|discovery|settings)\b|help\.skool\.com|"
    r"chatgpt\.com/g/|docs\.google\.com/(document|spreadsheets)/d/(1alukftm|1096vhdr|130dIL2H|1X4pEQC2|1mMiFuiS)|"
    r"manychat\.com|obsproject\.com|acquisition\.com)", re.I)
DICT = set()
if os.path.exists("/usr/share/dict/words"):
    DICT = {w.strip() for w in open("/usr/share/dict/words") if w.strip().islower()}


def pseudonym(uid):
    return "Member " + hashlib.sha1(uid.encode()).hexdigest()[:4]


def roster(posts_dir):
    users = {}

    def walk(n):
        p = n.get("post") or {}
        u = p.get("user")
        if u and u.get("id"):  # posts use firstName/lastName, the comments API uses first_name/last_name: merge both
            prev = users.get(u["id"], {})
            first = u.get("firstName") or u.get("first_name") or prev.get("firstName") or ""
            last = u.get("lastName") or u.get("last_name") or prev.get("lastName") or ""
            meta = {**(prev.get("metadata") or {}), **{k: v for k, v in (u.get("metadata") or {}).items() if v}}
            users[u["id"]] = {"id": u["id"], "firstName": first, "lastName": last,
                              "name": u.get("name") or prev.get("name") or "", "metadata": meta}
        for c in n.get("children") or []:
            walk(c)

    for f in glob.glob(os.path.join(posts_dir, "*.json")):
        if os.path.basename(f).startswith("_"):
            continue
        walk(json.load(open(f)))
    keep, members = {}, {}
    for uid, u in users.items():
        full = f"{(u.get('firstName') or '').strip()} {(u.get('lastName') or '').strip()}".strip()
        bio = (u.get("metadata") or {}).get("bio") or ""
        rec = {"id": uid, "full": full, "first": (u.get("firstName") or "").strip(), "last": (u.get("lastName") or "").strip(),
               "handle": u.get("name") or "", "links": [v for k, v in (u.get("metadata") or {}).items() if k.startswith("link") and v]}
        (keep if (full in KEEP_NAMES or STAFF_BIO.search(bio)) else members)[uid] = rec
    return keep, members


def build_rules(keep, members):
    keep_firsts = {r["first"] for r in keep.values()} | {n.split()[0] for n in KEEP_NAMES}
    first_count = {}
    for r in members.values():
        first_count[r["first"]] = first_count.get(r["first"], 0) + 1
    rules = []  # (compiled regex, replacement), longest patterns first
    for r in sorted(members.values(), key=lambda r: -len(r["full"])):
        p = pseudonym(r["id"])
        if r["full"]:
            rules.append((re.compile(re.escape(r["full"])), p))
        if r["first"] and r["last"]:
            last_words = r["last"].split()
            initials = r"\s+".join(re.escape(w[0]) + r"\." for w in last_words)  # "Alejandro L. R."
            rules.append((re.compile(r"\b" + re.escape(r["first"]) + r"\s+" + initials + r"(?!\w)"), p))
            if len(last_words[0]) >= 2:  # "Nick Sa." style, used to tell same-first-name members apart
                rules.append((re.compile(r"\b" + re.escape(r["first"]) + r"\s+" + re.escape(last_words[0][:2]) + r"\.(?!\w)"), p))
            rules.append((re.compile(r"\b" + re.escape(r["first"]) + r"\s+" + re.escape(r["last"][0]) + r"\.(?!\w)"), p))
        if len(r["last"]) >= 3 and r["last"].lower() not in DICT and r["last"] not in keep_firsts:
            rules.append((re.compile(r"\b" + re.escape(r["last"]) + r"\b"), p))
        if r["handle"]:
            rules.append((re.compile(r"\b" + re.escape(r["handle"]) + r"\b"), p.lower().replace(" ", "-")))
        f = r["first"]
        if len(f) >= 3 and f.lower() not in DICT and f not in keep_firsts:
            rules.append((re.compile(r"\b" + re.escape(f) + r"\b"), p if first_count[f] == 1 else "a member"))
    return rules


URL_RE = re.compile(r"https?://[^\s)\]>\"']+")
MD_LINK = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+|obj://[^)\s]+)\)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?<![\w$])\+?\d{1,2}[\s.-]?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\w)")
HANDLE = re.compile(r"(?<![\w/])@(?!Member\b)([A-Za-z0-9_.]{3,30})")
IMG_SECTION = re.compile(r"\n## Images\n\n(?:.*\n)*?(?=\n## |\Z)")


def scrub_text(t, rules, keep):
    t = MD_LINK.sub(lambda m: m.group(0) if ALLOWED_URL.match(m.group(2)) else (m.group(1) or "[link removed]"), t)
    t = URL_RE.sub(lambda m: m.group(0) if ALLOWED_URL.match(m.group(0)) else "[link removed]", t)
    t = EMAIL.sub("[email removed]", t)
    t = PHONE.sub("[phone removed]", t)
    for rx, rep in rules:
        t = rx.sub(rep, t)
    keep_handles = {r["handle"].lower() for r in keep.values()}
    t = HANDLE.sub(lambda m: m.group(0) if m.group(1).lower() in keep_handles else "@[handle]", t)
    t = IMG_SECTION.sub("\n## Images\n\n_Post images are not included in the public package (member screenshots)._\n", t)
    t = re.sub(r"!\[post image\]\([^)]*\)", "", t)
    return t


def main():
    args = sys.argv[1:]
    redact = []  # --redact "Brand Name": extra strings (your own brand, nicknames) replaced with [member brand]
    while "--redact" in args:
        i = args.index("--redact"); redact.append(args[i + 1]); del args[i:i + 2]
    posts_dir, md_dir, extra = args[0], args[1], args[2:]
    keep, members = roster(posts_dir)
    rules = [(re.compile(r"\b" + re.escape(s) + r"\b", re.I), "[member brand]") for s in sorted(redact, key=len, reverse=True)]
    rules += build_rules(keep, members)
    files = [f for f in glob.glob(os.path.join(md_dir, "**", "*.md"), recursive=True)] + extra
    changed = 0
    for f in files:
        t = open(f).read()
        s = scrub_text(t, rules, keep)
        if s != t:
            open(f, "w").write(s); changed += 1
    print("kept (staff, host, mentors):", sorted(r["full"] for r in keep.values()))
    print("members pseudonymized:", len(members), "| files changed:", changed, "of", len(files))
    json.dump({"members": [{"full": r["full"], "first": r["first"], "last": r["last"], "handle": r["handle"], "id": r["id"],
                            "links": r["links"]} for r in members.values()]},
              open(os.path.join(posts_dir, "_private_roster.json"), "w"))  # stays next to the private pull, never shipped


if __name__ == "__main__":
    main()
