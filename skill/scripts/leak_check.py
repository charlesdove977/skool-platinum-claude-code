"""Leak check for the public skill: no community member identity may survive the scrub.

usage: python3 -I leak_check.py <_private_roster.json> <dir> [--identity "Name" ...]

Scans every text file under <dir> for each pseudonymized member's full name, distinctive last name, Skool handle,
user id and personal links, plus Skool profile ids, emails, local paths and any --identity strings you pass
(your own name, brand, domains). Prints each hit as  file:line  pattern | context  and exits 1 on any hit.
"""
import json, os, re, sys

TEXT_EXT = {".md", ".txt", ".csv", ".py", ".sh", ".json", ".yaml", ".yml", ".html"}
DICT = set()
if os.path.exists("/usr/share/dict/words"):
    DICT = {w.strip() for w in open("/usr/share/dict/words") if w.strip().islower()}


def patterns(roster, identities):
    pats = []
    for m in roster["members"]:
        if m["full"]:
            pats.append(("name", re.compile(re.escape(m["full"]))))
        if len(m["last"]) >= 4 and m["last"].lower() not in DICT:
            pats.append(("last-name", re.compile(r"\b" + re.escape(m["last"]) + r"\b")))
        if m["handle"] and not m["handle"].isdigit():
            pats.append(("handle", re.compile(r"\b" + re.escape(m["handle"]) + r"\b")))
        pats.append(("user-id", re.compile(m["id"])))
        for link in m["links"]:
            core = re.sub(r"^https?://(www\.)?", "", link).rstrip("/")
            if len(core) > 8 and "/" in core:  # a bare domain like facebook.com is not personal
                pats.append(("member-link", re.compile(re.escape(core), re.I)))
    pats += [
        ("profile-id", re.compile(r"obj://user/|skool\.com/@[0-9a-f]{32}")),
        ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.(com|io|net|org|co|ai)\b")),
        ("local-path", re.compile(r"/Users/[A-Za-z]|C:\\\\Users\\\\")),
    ]
    for s in identities:
        pats.append(("identity", re.compile(re.escape(s), re.I)))
    return pats


def main():
    args = sys.argv[1:]
    identities = []
    while "--identity" in args:
        i = args.index("--identity"); identities.append(args[i + 1]); del args[i:i + 2]
    roster = json.load(open(args[0])); root = args[1]
    pats = patterns(roster, identities)
    hits = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in (".git", "__pycache__", ".base-ast")]
        for f in fn:
            path = os.path.join(dp, f)
            if os.path.splitext(f)[1].lower() not in TEXT_EXT:
                continue
            for n, line in enumerate(open(path, encoding="utf-8", errors="ignore"), 1):
                rel = os.path.relpath(path, root)
                course = any(s in "/" + rel for s in ("/source/classroom/", "/source/transcripts/"))  # verbatim course content: mentors and lesson text
                for kind, rx in pats:
                    if course and kind in ("last-name", "profile-id"):
                        continue
                    if "/scripts/" in "/" + rel and kind in ("last-name", "profile-id"):
                        continue
                    if rx.search(line):
                        hits += 1
                        print(f"HIT {os.path.relpath(path, root)}:{n} {kind}:{rx.pattern[:40]} | {line.strip()[:120]}")
    print(f"{hits} hits")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
