"""Publish articles to fintechtelex.com via WordPress REST API.
Run inside: pplx credentials run <handle> -- python3 publish.py [--status publish|draft]"""
import sys, json, requests
sys.path.insert(0,'posts')
from articles import ARTICLES
API="https://fintechtelex.com/wp-json/wp/v2"
status = sys.argv[sys.argv.index('--status')+1] if '--status' in sys.argv else 'publish'
S=requests.Session(); S.headers['User-Agent']='FintechTelexPublisher/1.0'
def tag_ids(names):
    ids=[]
    for n in names:
        r=S.get(f"{API}/tags",params={"search":n,"per_page":20}).json()
        m=[t for t in r if t['name'].lower()==n.lower()]
        if m: ids.append(m[0]['id']); continue
        c=S.post(f"{API}/tags",json={"name":n})
        if c.ok: ids.append(c.json()['id'])
    return ids
results=json.load(open('published.json')) if __import__('os').path.exists('published.json') else {}
for a in ARTICLES:
    if a['slug'] in results: print("skip",a['slug']); continue
    with open(f"images/{a['slug']}.png","rb") as fh:
        m=S.post(f"{API}/media",data=fh.read(),headers={"Content-Type":"image/png","Content-Disposition":f'attachment; filename="{a["slug"]}.png"'})
    m.raise_for_status(); mid=m.json()['id']
    S.post(f"{API}/media/{mid}",json={"alt_text":a['title'],"caption":"Fintech Telex"})
    p=S.post(f"{API}/posts",json={"title":a['title'],"slug":a['slug'],"content":a['html'].strip(),"excerpt":a['excerpt'],
        "status":status,"categories":a['cats'],"tags":tag_ids(a['tags']),"featured_media":mid,"author":2478})
    if p.status_code==403 or (not p.ok and 'author' in p.text):
        p=S.post(f"{API}/posts",json={"title":a['title'],"slug":a['slug'],"content":a['html'].strip(),"excerpt":a['excerpt'],
            "status":status,"categories":a['cats'],"tags":tag_ids(a['tags']),"featured_media":mid})
    p.raise_for_status(); j=p.json()
    results[a['slug']]={"id":j['id'],"link":j['link'],"status":j['status'],"media":mid}
    json.dump(results,open('published.json','w'),indent=1)
    print(j['status'],j['link'])
