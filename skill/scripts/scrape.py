"""Read-only scrape of Platinum (October) classroom pages. GET requests only."""
import http.cookiejar, json, os, re, sys, time, urllib.request

SCR = os.path.dirname(os.path.abspath(__file__))
JAR = os.path.expanduser(os.environ.get("SKOOL_COOKIES", "~/.skool_cookies.txt"))  # Netscape-format cookie jar exported from your logged-in skool.com browser session
OUT = os.environ.get("PLATINUM_OUT") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "source")  # default: the skill's source/ folder
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
REF = {"Referer": "https://www.skool.com/", "Origin": "https://www.skool.com", "User-Agent": UA}

cj = http.cookiejar.MozillaCookieJar(JAR); cj.load(ignore_discard=True, ignore_expires=True)
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

def get(url, headers=None):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=headers or {"User-Agent": UA})
            return opener.open(req, timeout=60).read().decode("utf-8", "replace")
        except Exception as e:
            print("  retry", attempt, url[:80], e); time.sleep(3 * (attempt + 1))
    raise RuntimeError(url)

UNKNOWN = set()
def inline(nodes):
    s = ""
    for n in nodes or []:
        t = n.get("type")
        if t == "text":
            x = n.get("text", "")
            for m in n.get("marks") or []:
                mt = m["type"]
                if mt == "bold": x = f"**{x}**"
                elif mt == "italic": x = f"*{x}*"
                elif mt == "code": x = f"`{x}`"
                elif mt == "link": x = f"[{x}]({m['attrs'].get('href')})"
                elif mt in ("underline", "strike", "textStyle", "highlight"): pass
                else: UNKNOWN.add("mark:" + mt)
            s += x
        elif t == "hardBreak": s += "  \n"
        elif t == "image": s += f"![image]({(n.get('attrs') or {}).get('src')})"
        elif t == "emoji": s += (n.get("attrs") or {}).get("emoji", "")
        else:
            UNKNOWN.add(t); s += inline(n.get("content"))
    return s

def block(n, ind=""):
    t = n.get("type"); a = n.get("attrs") or {}; c = n.get("content") or []
    if t == "paragraph": return ind + inline(c)
    if t == "heading": return "#" * min(6, a.get("level", 2) + 1) + " " + inline(c)
    if t in ("bulletList", "orderedList", "unorderedList"):
        out = []
        for i, li in enumerate(c, 1):
            mark = f"{i}." if t == "orderedList" else "-"
            parts = [block(x, ind + "   ").strip() if j else block(x, "").strip() for j, x in enumerate(li.get("content") or [])]
            out.append(ind + f"{mark} " + ("\n" + ind + "   ").join(p for p in parts if p) if False else ind + f"{mark} " + "\n".join(parts))
        return "\n".join(out)
    if t == "blockquote": return "\n".join("> " + l for l in "\n\n".join(block(x) for x in c).splitlines())
    if t == "codeBlock": return "```\n" + "".join(x.get("text", "") for x in c) + "\n```"
    if t == "horizontalRule": return "---"
    if t == "image": return f"![image]({a.get('src')})"
    if t in ("videoEmbed", "embed", "youtube", "iframe", "video"): return f"[embedded {t}: {a.get('src') or a.get('url') or a}]"
    UNKNOWN.add(t)
    return "\n\n".join(block(x, ind) for x in c) if c else f"[{t}: {a}]"

def desc_md(desc):
    if not desc: return ""
    if desc.startswith("[v2]"):
        try: return "\n\n".join(block(n) for n in json.loads(desc[4:]))
        except Exception as e: return f"[unparsed desc: {e}]\n{desc}"
    return desc

def page_props(slug_id, md=None):
    url = f"https://www.skool.com/platinum-october/classroom/{slug_id}" + (f"?md={md}" if md else "")
    h = get(url)
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', h, re.S)
    return json.loads(m.group(1))["props"]["pageProps"]

def walk(n, path, out):
    c = n.get("course", n); md = c.get("metadata", {})
    if c.get("unitType") == "module": out.append((path, c["id"], md.get("title")))
    for ch in n.get("children") or []:
        cc = ch.get("course", ch)
        walk(ch, path + ([cc["metadata"].get("title")] if cc.get("unitType") == "set" else []), out)
    return out

def find(n, i):
    c = n.get("course", n)
    if c.get("id") == i: return c
    for ch in n.get("children") or []:
        r = find(ch, i)
        if r: return r

manifest = []
for root in sys.argv[1:]:
    base = json.load(open(f"{SCR}/plat/{root}.json"))
    course_title = base["course"]["course"]["metadata"]["title"]
    pages = walk(base["course"], [], [])
    print(f"== {course_title}: {len(pages)} pages")
    for idx, (path, pid, title) in enumerate(pages, 1):
        cache = f"{SCR}/plat/page_{pid}.json"
        if os.path.exists(cache): pp = json.load(open(cache))
        else:
            pp = page_props(root, pid); json.dump(pp, open(cache, "w")); time.sleep(0.8)
        mod = find(pp["course"], pid); md = mod["metadata"]
        v = pp.get("video") if (pp.get("video") or {}).get("id") == md.get("videoId") else None
        rec = {
            "classroom": course_title, "root": root, "order": idx, "folder": " / ".join(path),
            "id": pid, "title": title, "url": f"https://www.skool.com/platinum-october/classroom/{root}?md={pid}",
            "video_link": md.get("videoLink") or "", "video_id": md.get("videoId") or "",
            "video_len_ms": md.get("videoLenMs") or (v or {}).get("duration") or "",
            "mux": {"playbackId": v["playbackId"], "token": v["playbackToken"]} if v else None,
            "resources": json.loads(md.get("resources") or "[]"),
            "desc_md": desc_md(md.get("desc") or ""),
        }
        manifest.append(rec)
        print(f"  {idx:02d} {title[:50]:50s} desc={len(rec['desc_md']):5d} res={len(rec['resources'])} vid={'mux' if v else ('link' if rec['video_link'] else ('MISSING' if rec['video_id'] else '-'))}")

json.dump(manifest, open(f"{SCR}/plat/manifest.json", "w"), indent=1)
print("unknown node types:", UNKNOWN)
