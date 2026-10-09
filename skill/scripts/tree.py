import re,json,sys
for id in sys.argv[1:]:
    h=open(f"plat/{id}.html").read()
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
    d=json.loads(m.group(1)); pp=d["props"]["pageProps"]
    json.dump(pp,open(f"plat/{id}.json","w"))
    c=pp.get("course") or {}
    def walk(n,depth,out):
        cc=n.get("course",n); md=cc.get("metadata",{})
        out.append(("  "*depth)+f"[{cc.get('unitType')}] {md.get('title')} | id={cc.get('id')} | vid={md.get('videoId','')} | link={md.get('videoLink','')} | len={md.get('videoLenMs','')} | desclen={len(md.get('desc') or '')}")
        for ch in n.get("children") or []: walk(ch,depth+1,out)
        return out
    print("=====",id, list(pp.keys()))
    print("\n".join(walk(c,0,[])))
