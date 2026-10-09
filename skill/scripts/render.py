"""Render scraped Platinum data into markdown under the repo source folder. Read-only against Skool."""
import datetime, json, glob, os, re, time, urllib.request

TODAY = __import__("datetime").date.today().isoformat()
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("PLATINUM_OUT") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "source")  # default: the skill's source/ folder
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def slug(s): return re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")[:60] or "untitled"
def get(url, binary=False):
    for a in range(3):
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://www.skool.com/"}), timeout=60).read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:
            last = e; time.sleep(2 * (a + 1))
    raise last
def save_img(url, d, fn):
    os.makedirs(d, exist_ok=True)
    have = [f for f in os.listdir(d) if f.startswith(fn + ".")]
    if have: return f"{d}/{have[0]}"
    b = get(url, binary=True)
    ext = "png" if b[:4] == b"\x89PNG" else "gif" if b[:3] == b"GIF" else "webp" if b[8:12] == b"WEBP" else "jpg"
    open(f"{d}/{fn}.{ext}", "wb").write(b); return f"{d}/{fn}.{ext}"

# ---------- lessons ----------
manifest = json.load(open(f"{SCR}/plat/manifest.json"))
lesson_files = []
for r in manifest:
    d = f"{OUT}/classroom/{slug(r['classroom'])}"; os.makedirs(d, exist_ok=True)
    body = r["desc_md"]
    imgs = r.get("images") or []
    i = 0
    def rep(m):
        global i
        return m.group(0)
    for n, local in enumerate(imgs, 1):  # swap remote asset urls for local relative paths, in order
        body = re.sub(r"!\[image\]\((https://assets\.skool\.com[^)]+|https://embed\.filekitcdn[^)]+)\)",
                      f"![image {n}](images/{slug(r['classroom'])}/{os.path.basename(local)})", body, count=1)
    tdir = f"{OUT}/transcripts/{slug(r['classroom'])}"
    trs = sorted(os.path.basename(t) for t in glob.glob(f"{tdir}/{r['order']:02d}-*.md"))
    fm = (f"---\ntype: lesson\nclassroom: {r['classroom']}\nfolder: {r['folder']}\norder: {r['order']}\n"
          f"source_page: {r['url']}\nvideo: {r['video_link'] or ('skool-native' if r['mux'] else 'none')}\n"
          f"images: {len(imgs)}\ntranscripts: [{', '.join(trs)}]\npulled: {TODAY}\n---\n\n")
    md = fm + f"# {r['title']}\n\n_{r['classroom']} / {r['folder']}_\n\n" + (body or "_No page text._") + "\n"
    if trs: md += "\n## Video transcripts\n\n" + "\n".join(f"- [../../transcripts/{slug(r['classroom'])}/{t}](../../transcripts/{slug(r['classroom'])}/{t})" for t in trs) + "\n"
    p = f"{d}/{r['order']:02d}-{slug(r['title'])}.md"; open(p, "w").write(md); lesson_files.append(p)
print("lessons:", len(lesson_files))

# ---------- community posts ----------
grp = json.load(open(f"{SCR}/posts/_group.json"))
labels = {}
for m in re.finditer(r'\{"id": "([0-9a-f]{32})", "metadata": \{[^{}]*?"displayName": "((?:[^"\\]|\\.)*)"', json.dumps(grp)):
    labels[m.group(1)] = json.loads('"' + m.group(2) + '"').strip()
feed = json.load(open(f"{SCR}/posts/_feed.json"))
def who(u): u = u or {}; return (f"{u.get('firstName') or u.get('first_name') or ''} {u.get('lastName') or u.get('last_name') or ''}".strip() or u.get("name") or "unknown")
def when(ts): return (ts or "")[:10]
def post_images(meta, d, base):
    urls = []
    for k in ("imagePreview",):
        if meta.get(k): urls.append(meta[k])
    for k in ("attachmentsData", "attachments_data"):
        try:
            for a in json.loads(meta.get(k) or "[]"):
                u = (a.get("metadata") or {}).get("url") or a.get("url") or (a.get("metadata") or {}).get("image")
                if u: urls.append(u)
        except Exception: pass
    urls += re.findall(r"https://assets\.skool\.com/f/[^\s)\"']+", meta.get("content") or "")
    out, seen = [], set()
    for n, u in enumerate([u for u in urls if not (u in seen or seen.add(u))], 1):
        if "picture_" in u or u.endswith("-sm.jpg"): continue
        try: out.append(save_img(u, d, f"{base}-{n}"))
        except Exception as e: out.append(f"FAILED {u}: {e}")
    return out
def render_comments(children, depth=0):
    s = ""
    for c in children or []:
        cp = c["post"]; m = cp["metadata"]
        txt = (m.get("content") or "").strip().replace("\n", "\n" + "  " * depth + "  ")
        s += f"{'  ' * depth}- **{who(cp.get('user'))}** ({when(cp.get('createdAt'))}, {m.get('upvotes', 0)} likes): {txt}\n"
        s += render_comments(c.get("children"), depth + 1)
    return s
post_files, index_rows, img_count = [], [], 0
for p in feed:
    f = f"{SCR}/posts/{p['id']}.json"
    tree = json.load(open(f)) if os.path.exists(f) else {"post": p, "children": []}
    post = tree.get("post") or p; m = post["metadata"]
    lab = labels.get(post.get("labelId") or m.get("labels") or "", "Uncategorized")
    d = f"{OUT}/community/{slug(lab)}"; os.makedirs(d, exist_ok=True)
    base = f"{when(post.get('createdAt'))}-{slug(m.get('title'))}"
    imgs = post_images(m, f"{OUT}/community/images", base); img_count += len([x for x in imgs if not x.startswith("FAILED")])
    def _count(ch): return sum(1 + _count(c.get("children")) for c in ch or [])
    ncom = _count(tree.get("children"))
    md = (f"---\ntype: community-post\ncategory: {lab}\nauthor: {who(post.get('user'))}\ndate: {when(post.get('createdAt'))}\n"
          f"pinned: {bool(m.get('pinned'))}\nlikes: {m.get('upvotes', 0)}\ncomments: {m.get('comments', 0)}\ncomments_captured: {ncom}\n"
          f"source: https://www.skool.com/platinum-october/{post['name']}\npulled: {TODAY}\n---\n\n# {m.get('title')}\n\n"
          + (m.get("content") or "").strip() + "\n")
    if m.get("videoLinksData") or m.get("videoLinks"): md += f"\n_Video in post: {m.get('videoLinks') or m.get('videoLinksData')}_\n"
    if m.get("pollOptions") or m.get("poll"): md += f"\n_Poll: {m.get('pollOptions') or m.get('poll')}_\n"
    if imgs: md += "\n## Images\n\n" + "\n".join(f"![post image](../images/{os.path.basename(x)})" if not x.startswith("FAILED") else f"- {x}" for x in imgs) + "\n"
    cm = render_comments(tree.get("children"))
    if cm: md += "\n## Comments\n\n" + cm
    pf = f"{d}/{base}.md"; open(pf, "w").write(md); post_files.append(pf)
    index_rows.append((when(post.get("createdAt")), lab, m.get("title"), who(post.get("user")), m.get("upvotes", 0), m.get("comments", 0), bool(m.get("pinned")), os.path.relpath(pf, f"{OUT}/community")))
index_rows.sort(key=lambda r: (not r[6], r[0]), reverse=False)
idx = "# Platinum (October) community feed\n\nPulled " + TODAY + ", read-only. " + f"{len(post_files)} posts, {img_count} post images.\n\n| Date | Category | Title | Author | Likes | Comments | File |\n|---|---|---|---|---|---|---|\n"
for r in sorted(index_rows, key=lambda r: r[0], reverse=True):
    idx += f"| {r[0]} | {r[1]} | {'📌 ' if r[6] else ''}{(r[2] or '').replace('|', '/')} | {r[3]} | {r[4]} | {r[5]} | [{os.path.basename(r[7])}]({r[7]}) |\n"
open(f"{OUT}/community/INDEX.md", "w").write(idx)
print("posts:", len(post_files), "post images:", img_count, "labels:", labels)

# ---------- linked Google Docs / Sheets (public exports) ----------
gd = f"{OUT}/linked-docs"; os.makedirs(gd, exist_ok=True); got = []
for r in manifest:
    for u in set(re.findall(r"https://docs\.google\.com/(document|spreadsheets)/d/([\w-]+)", r["desc_md"])):
        kind, did = u
        exp = f"https://docs.google.com/document/d/{did}/export?format=txt" if kind == "document" else f"https://docs.google.com/spreadsheets/d/{did}/export?format=csv"
        fn = f"{gd}/{slug(r['title'])}-{did[:8]}.{'txt' if kind == 'document' else 'csv'}"
        try:
            t = get(exp)
            if "<html" in t[:500].lower(): raise RuntimeError("not public (login page)")
            open(fn, "w").write(f"# source: https://docs.google.com/{kind}/d/{did} (linked from lesson '{r['title']}')\n\n" + t); got.append((r["title"], fn, len(t)))
        except Exception as e: got.append((r["title"], f"FAILED {did}: {e}", 0))
for g in got: print("doc:", g)
