import sys; sys.path.insert(0,'posts/2026-11-27')
from articles import ARTICLES
from PIL import Image, ImageDraw, ImageFont
B="/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"; R="/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
ACC={"DIASPORA VOICE":(232,163,23),"FINANCE":(22,163,74),"CRYPTO NEWS":(247,147,26),"BUSINESS":(37,99,235),
     "SECURITY NEWS":(220,38,38),"ARTIFICIAL INTELLIGENCE":(147,51,234),"SPORTS":(5,150,105),"TECH NEWS":(14,165,233),
     "NIGERIA NEWS":(0,135,81),"NIGERIA POLITICS":(190,18,60),"ENTERTAINMENT":(219,39,119)}
W,H=1200,675
import os; os.makedirs('images/2026-11-27',exist_ok=True)
for a in ARTICLES:
    acc=ACC[a['label']]
    im=Image.new("RGB",(W,H),(11,18,32)); d=ImageDraw.Draw(im)
    for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(17,26,44))
    for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(17,26,44))
    d.rectangle([0,0,14,H],fill=acc)
    f=ImageFont.truetype(B,26); lab=a['label']
    tw=d.textlength(lab,font=f); d.rectangle([70,70,70+tw+36,70+50],fill=acc); d.text((88,78),lab,font=f,fill=(255,255,255))
    for size in (60,56,52,48,44,40):
        ft=ImageFont.truetype(B,size); lines=[]; words=a['title'].split(); cur=""
        for w in words:
            t=(cur+" "+w).strip()
            if d.textlength(t,font=ft)<=W-150: cur=t
            else: lines.append(cur); cur=w
        lines.append(cur)
        if len(lines)*size*1.22<=360: break
    y=160
    for l in lines: d.text((70,y),l,font=ft,fill=(248,250,252)); y+=int(size*1.22)
    d.line([(70,H-95),(W-70,H-95)],fill=(51,65,85),width=2)
    d.text((70,H-78),"FINTECH TELEX",font=ImageFont.truetype(B,30),fill=acc)
    fr=ImageFont.truetype(R,24); s="fintechtelex.com  |  November 27, 2026"
    d.text((W-70-d.textlength(s,font=fr),H-72),s,font=fr,fill=(148,163,184))
    im.save(f"images/2026-11-27/{a['slug']}.png",optimize=True); print(a['slug'],len(lines),size)
