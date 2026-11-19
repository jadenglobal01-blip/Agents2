import json,glob,re,collections,sys
import sys; D=sys.argv[1] if len(sys.argv)>1 else "./pages/"
pages=collections.defaultdict(dict)
for f in glob.glob(D+"*.txt"):
    try: o=json.load(open(f))
    except Exception: continue
    c=o["contents"][0]; u=c["uri"]
    m=re.search(r"datasets/(\w+)/items.*offset=(\d+)",u)
    if not m: continue
    pages[m.group(1)][int(m.group(2))]=json.loads(c["text"])
for ds,p in sorted(pages.items()):
    print(ds,{k:len(v) for k,v in sorted(p.items())})

import csv,os,statistics
OUT="/home/user/Agents2/data/apify/2026-11-18"; os.makedirs(OUT,exist_ok=True)
META={"aRS8bmZkvJKRKaVc9":("5z5yzRflh00d2Cy2D","hashtag","tiktok-scraper"),
"mwIDgluGcsZvV6BKH":("huogeJgeQ9ltatxuj","profile","tiktok-profile-scraper"),
"tsO5GnuzPcPJIMk37":("nCzM9Ds3Xl1gARQBj","hashtag","tiktok-scraper"),
"LDDH9ckaB9buMDhwF":("D99n38320uQzjvgNL","profile","tiktok-profile-scraper"),
"SxsYuSsiInJCvpys7":("NU2yMH3IiwvDUcOw7","hashtag","tiktok-scraper"),
"stl0FevTDoKG0GGEk":("542hNx4mx61ZwRe9c","profile","tiktok-profile-scraper")}
rows=[]
for ds,p in pages.items():
    items=[i for k in sorted(p) for i in p[k]]
    json.dump(items,open(f"{OUT}/raw_{META[ds][1]}_{ds}.json","w"),ensure_ascii=False,indent=1)
    for i in items:
        i["_dataset"]=ds; i["_source"]=META[ds][1]; rows.append(i)
cols=["_source","_dataset","input","authorMeta.name","id","webVideoUrl","createTimeISO","playCount","diggCount","commentCount","shareCount","collectCount","isAd","isSponsored","text"]
with open(f"{OUT}/videos.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=cols,extrasaction="ignore"); w.writeheader(); w.writerows(rows)
EM=re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
cr={}
for r in rows:
    n=r.get("authorMeta.name")
    if not n: continue
    c=cr.setdefault(n,{"username":n,"vids":[],"tags":set(),"src":set()})
    for k in ["nickName","fans","heart","video","verified","signature","bioLink","profileUrl"]:
        v=r.get("authorMeta."+k)
        if v is not None: c[k]=v
    c["src"].add(r["_source"])
    if r["_source"]=="hashtag": c["tags"].add(r.get("input",""))
    c["vids"].append(r)
out=[]
for c in cr.values():
    prof=[v for v in c["vids"] if v["_source"]=="profile"] or c["vids"]
    plays=[v.get("playCount") or 0 for v in prof]
    eng=[((v.get("diggCount") or 0)+(v.get("commentCount") or 0)+(v.get("shareCount") or 0)+(v.get("collectCount") or 0))/v["playCount"] for v in prof if v.get("playCount")]
    sig=c.get("signature") or ""
    out.append({"username":c["username"],"nickname":c.get("nickName",""),"followers":c.get("fans",""),"total_likes":c.get("heart",""),"video_count":c.get("video",""),"verified":c.get("verified",""),
      "email":";".join(sorted(set(EM.findall(sig)))),"bio_link":c.get("bioLink") or "","profile_url":c.get("profileUrl",""),
      "median_views_recent":int(statistics.median(plays)) if plays else "","avg_engagement_rate":round(statistics.mean(eng),4) if eng else "",
      "sample_videos":len(prof),"has_profile_scrape":"profile" in c["src"],"found_via_hashtags":";".join(sorted(c["tags"])),
      "last_post":max((v.get("createTimeISO") or "") for v in c["vids"])[:10],"bio":sig.replace("\n"," | ")})
out.sort(key=lambda x:(not x["has_profile_scrape"],-(x["followers"] or 0)))
with open(f"{OUT}/creators.csv","w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
print("videos",len(rows),"creators",len(out),"profile-scraped",sum(x["has_profile_scrape"] for x in out),"with email",sum(bool(x["email"]) for x in out),
      "profile+email",sum(bool(x["email"]) and x["has_profile_scrape"] for x in out))
