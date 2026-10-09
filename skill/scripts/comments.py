"""Read-only: fetch full comment trees for every post via api2 GET and merge into posts/{id}.json."""
import http.cookiejar, json, os, time, urllib.request
SCR=os.path.dirname(os.path.abspath(__file__))
JAR = os.path.expanduser(os.environ.get("SKOOL_COOKIES", "~/.skool_cookies.txt"))  # Netscape-format cookie jar exported from your logged-in skool.com browser session
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
GID="842bb35fe5074be9a4163225bca792f0"
cj=http.cookiejar.MozillaCookieJar(JAR); cj.load(ignore_discard=True, ignore_expires=True)
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
def get(u):
    for a in range(4):
        try: return json.loads(op.open(urllib.request.Request(u,headers={"User-Agent":UA,"Origin":"https://www.skool.com","Referer":"https://www.skool.com/"}),timeout=60).read())
        except Exception as e: print(" retry",a,e); time.sleep(4*(a+1))
    return {}
def count(ch): return sum(1+count(c.get("children")) for c in ch or [])
feed=json.load(open(f"{SCR}/posts/_feed.json")); tot_exp=tot_got=0
for p in feed:
    n=p["metadata"].get("comments",0)
    if not n: continue
    f=f"{SCR}/posts/{p['id']}.json"; tree=json.load(open(f))
    if tree.get("_comments_fetched"): tot_exp+=n; tot_got+=count(tree.get("children")); continue
    children=[]; seen=set(); d={}
    # API caps limit at 30 and has no working cursor; head + tail covers threads with up to 60 top-level comments
    for q in ("limit=30&pinned=true", "limit=30&tail=true"):
        d=get(f"https://api2.skool.com/posts/{p['id']}/comments?group-id={GID}&{q}")
        for c in (d.get("post_tree") or {}).get("children") or []:
            if c["post"]["id"] not in seen: seen.add(c["post"]["id"]); children.append(c)
        time.sleep(0.7)
    tree["children"]=children; tree["_comments_fetched"]=True
    json.dump(tree,open(f,"w")); got=count(children); tot_exp+=n; tot_got+=got
    print(f"{n:4d} expected {got:4d} got  {p['metadata'].get('title','')[:60]}",flush=True); time.sleep(0.7)
print("TOTAL expected",tot_exp,"got",tot_got)
