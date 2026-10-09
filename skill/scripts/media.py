"""Read-only media pull: images + transcripts for every video in manifest.json."""
import json, os, re, subprocess, sys, time, urllib.request

TODAY = __import__("datetime").date.today().isoformat()
SCR = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("PLATINUM_OUT") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "source")  # default: the skill's source/ folder
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
H = {"Referer": "https://www.skool.com/", "Origin": "https://www.skool.com", "User-Agent": UA}
WORK = f"{SCR}/media"; os.makedirs(WORK, exist_ok=True)

def get(url, binary=False):
    for a in range(4):
        try:
            b = urllib.request.urlopen(urllib.request.Request(url, headers=H), timeout=120).read()
            return b if binary else b.decode("utf-8", "replace")
        except Exception as e:
            print("   retry", a, e); time.sleep(3 * (a + 1))
    raise RuntimeError(url)

def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]
def ts(sec): sec = int(sec); return f"{sec//3600:01d}:{sec%3600//60:02d}:{sec%60:02d}"

def vtt_to_segments(vtt):
    segs, cur = [], None
    for line in vtt.splitlines():
        m = re.match(r"(\d+):(\d+):(\d+)[.,](\d+)\s+-->", line) or re.match(r"(\d+):(\d+)[.,](\d+)\s+-->", line)
        if m:
            g = [int(x) for x in m.groups()]
            start = g[0]*3600 + g[1]*60 + g[2] if len(g) == 4 else g[0]*60 + g[1]
            cur = [start, ""]; segs.append(cur); continue
        if cur is not None and line.strip() and not line.strip().isdigit() and not line.startswith(("WEBVTT", "NOTE", "X-TIMESTAMP")):
            cur[1] += " " + re.sub(r"<[^>]+>", "", line.strip())
    out, last, seen = [], "", set()
    for s, t in segs:  # drop rolling-caption and segment-overlap duplicates
        t = t.strip()
        if t and t != last and (s, t) not in seen: out.append((s, t)); last = t; seen.add((s, t))
    return out

def paragraphs(segs, window=45):
    paras, start, buf = [], None, []
    for s, t in segs:
        if start is None: start = s
        buf.append(t)
        if (s - start >= window and t.rstrip().endswith((".", "?", "!"))) or s - start >= 2 * window:
            paras.append(f"**[{ts(start)}]** " + " ".join(buf)); start, buf = None, []
    if buf: paras.append(f"**[{ts(start)}]** " + " ".join(buf))
    return "\n\n".join(paras)

def whisper(audio):
    from faster_whisper import WhisperModel
    model = WhisperModel("small.en", compute_type="int8")
    segments, _ = model.transcribe(audio, vad_filter=True)
    return [(s.start, s.text.strip()) for s in segments]

def mux(rec):
    pid, tok = rec["mux"]["playbackId"], rec["mux"]["token"]
    master = get(f"https://stream.mux.com/{pid}.m3u8?token={tok}")
    sub = re.search(r'TYPE=SUBTITLES[^\n]*URI="([^"]+)"', master)
    aud = re.search(r'TYPE=AUDIO[^\n]*URI="([^"]+)"', master)
    dur = 0.0
    if aud:
        for d in re.findall(r"#EXTINF:([\d.]+)", get(aud.group(1))): dur += float(d)
    if sub:
        pl = get(sub.group(1)); base = sub.group(1).rsplit("/", 1)[0]
        vtt = "".join(get(u if u.startswith("http") else f"{base}/{u}") for u in [l for l in pl.splitlines() if l and not l.startswith("#")])
        segs = vtt_to_segments(vtt)
        if segs: return segs, dur, "Mux auto-captions (English CC track)"
    audio = f"{WORK}/{rec['id']}.m4a"
    if not os.path.exists(audio):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-headers", "Referer: https://www.skool.com/\r\nOrigin: https://www.skool.com\r\n",
                        "-i", aud.group(1), "-vn", "-c", "copy", audio], check=True)
    return whisper(audio), dur, "local faster-whisper small.en"

def ytdlp(url, key):
    d = f"{WORK}/{key}"; os.makedirs(d, exist_ok=True)
    info = subprocess.run(["yt-dlp", "-J", "--no-warnings", url], capture_output=True, text=True)
    dur = (json.loads(info.stdout).get("duration") if info.returncode == 0 else 0) or 0
    title = json.loads(info.stdout).get("title", "") if info.returncode == 0 else ""
    subprocess.run(["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs", "--sub-langs", "en.*,en", "--sub-format", "vtt",
                    "-o", f"{d}/v.%(ext)s", url], capture_output=True, text=True)
    vtts = sorted(f for f in os.listdir(d) if f.endswith(".vtt"))
    vtts.sort(key=lambda f: (".en.vtt" not in f and "en-orig" not in f, f))
    if vtts:
        segs = vtt_to_segments(open(f"{d}/{vtts[0]}").read())
        if segs: return segs, dur, f"captions via yt-dlp ({vtts[0].split('.',1)[1]})", title
    subprocess.run(["yt-dlp", "-f", "ba/b", "-x", "--audio-format", "m4a", "-o", f"{d}/a.%(ext)s", url], capture_output=True, text=True)
    a = [f for f in os.listdir(d) if f.startswith("a.")]
    if not a: return [], dur, "FAILED: no captions and audio download failed", title
    return whisper(f"{d}/{a[0]}"), dur, "local faster-whisper small.en", title

def write_transcript(folder, name, header, segs):
    os.makedirs(folder, exist_ok=True)
    p = f"{folder}/{name}.md"
    open(p, "w").write(header + "\n\n## Transcript\n\n" + (paragraphs(segs) if segs else "_No transcript could be produced._") + "\n")
    return p

manifest = json.load(open(f"{SCR}/plat/manifest.json"))
only = set(sys.argv[1:])
report = []

# 1. images
if not only or "images" in only:
    for rec in manifest:
        urls = re.findall(r"!\[image\]\(([^)]+)\)", rec["desc_md"])
        for i, u in enumerate(urls, 1):
            if "assets.skool.com" not in u and "filekitcdn" not in u: continue
            d = f"{OUT}/classroom/images/{slug(rec['classroom'])}"; os.makedirs(d, exist_ok=True)
            fn = f"{rec['order']:02d}-{slug(rec['title'])}-{i}"
            existing = [f for f in os.listdir(d) if f.startswith(fn + ".")]
            if existing: rec.setdefault("images", []).append(f"{d}/{existing[0]}"); continue
            try:
                b = get(u, binary=True)
                ext = "png" if b[:4] == b"\x89PNG" else "gif" if b[:3] == b"GIF" else "webp" if b[8:12] == b"WEBP" else "jpg"
                open(f"{d}/{fn}.{ext}", "wb").write(b); rec.setdefault("images", []).append(f"{d}/{fn}.{ext}")
            except Exception as e: print("  IMG FAIL", rec["title"], e)
    json.dump(manifest, open(f"{SCR}/plat/manifest.json", "w"), indent=1)
    print("images done:", sum(len(r.get("images", [])) for r in manifest))

# 2. page videos + embedded YouTube
if not only or "videos" in only:
    for rec in manifest:
        jobs = []
        if rec["mux"]: jobs.append(("mux", None))
        if rec["video_link"]: jobs.append(("link", rec["video_link"]))
        for u in re.findall(r"\]\((https?://(?:www\.)?(?:youtu\.be|youtube\.com/watch)[^)]+)\)", rec["desc_md"]):
            if "convertkit" not in u: jobs.append(("embed", u))
        for kind, url in jobs:
            folder = f"{OUT}/transcripts/{slug(rec['classroom'])}"
            name = f"{rec['order']:02d}-{slug(rec['title'])}" + ("" if kind != "embed" else "-ref-" + re.sub(r"\W", "", url.split("v=")[-1].split("youtu.be/")[-1])[:11])
            if os.path.exists(f"{folder}/{name}.md"): print("  skip", name); continue
            print(f"  >> {rec['title']} [{kind}]", flush=True)
            t0 = time.time()
            try:
                if kind == "mux": segs, dur, src = mux(rec); vt = ""
                else: segs, dur, src, vt = ytdlp(url, f"{rec['id']}-{slug(url)[-20:]}")
            except Exception as e:
                segs, dur, src, vt = [], 0, f"FAILED: {e}", ""
            hdr = (f"---\ntype: transcript\nclassroom: {rec['classroom']}\nfolder: {rec['folder']}\nlesson: {rec['title']}\n"
                   f"source_page: {rec['url']}\nvideo: {url or 'skool-native (mux ' + rec['mux']['playbackId'][:8] + '...)'}\n"
                   f"{'video_title: ' + json.dumps(vt) + chr(10) if vt else ''}duration: {ts(dur)}\ntranscript_source: {src}\n"
                   f"pulled: {TODAY}\n---\n\n# {rec['title']}" + (" (referenced video)" if kind == "embed" else ""))
            p = write_transcript(folder, name, hdr, segs)
            words = sum(len(t.split()) for _, t in segs)
            report.append((rec["title"], kind, ts(dur), words, src))
            print(f"     {ts(dur)} {words} words via {src} ({time.time()-t0:.0f}s)", flush=True)
    json.dump(report, open(f"{SCR}/plat/media_report.json", "w"), indent=1)
    print("videos done")
