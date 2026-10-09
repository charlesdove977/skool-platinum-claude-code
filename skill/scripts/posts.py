"""Read-only: every community post + comment tree in platinum-october."""
import http.cookiejar, json, os, re, time, urllib.request
SCR=os.path.dirname(os.path.abspath(__file__))
JAR = os.path.expanduser(os.environ.get("SKOOL_COOKIES", "~/.skool_cookies.txt"))  # Netscape-format cookie jar exported from your logged-in skool.com browser session
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
cj=http.cookiejar.MozillaCookieJar(JAR); cj.load(ignore_discard=True, ignore_expires=True)
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
def pp(url):
    for a in range(4):
        try:
            h=op.open(urllib.request.Request(url,headers={"User-Agent":UA}),timeout=60).read().decode()
            return json.loads(re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S).group(1))["props"]["pageProps"]
        except Exception as e: print(" retry",a,e); time.sleep(4*(a+1))
os.makedirs(f"{SCR}/posts",exist_ok=True)
feed=[]; page=1
while True:
    d=pp(f"https://www.skool.com/platinum-october?p={page}")
    trees=d.get("postTrees") or []
    if page==1: json.dump({k:d.get(k) for k in ("currentGroup","settings")},open(f"{SCR}/posts/_group.json","w"))
    if not trees: break
    feed+= [t["post"] for t in trees]; print("feed page",page,len(trees),flush=True); page+=1; time.sleep(0.8)
    if len(feed)>=d.get("total",0): break
seen=set(); uniq=[p for p in feed if not (p["id"] in seen or seen.add(p["id"]))]
print("unique posts",len(uniq))
for i,p in enumerate(uniq,1):
    f=f"{SCR}/posts/{p['id']}.json"
    if os.path.exists(f): continue
    d=pp(f"https://www.skool.com/platinum-october/{p['name']}")
    json.dump(d.get("postTree") or d,open(f,"w")); time.sleep(0.8)
    if i%10==0: print(" fetched",i,flush=True)
json.dump(uniq,open(f"{SCR}/posts/_feed.json","w"))
print("done")
