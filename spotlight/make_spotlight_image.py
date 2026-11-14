import sys
from PIL import Image, ImageDraw, ImageFont
# usage: python3 make_spotlight_image.py "<title>" "<guide number>" "<Month D, YYYY>" <out.png>
title,num,date,out=sys.argv[1:5]
B="/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"; R="/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
acc=(212,175,55); W,H=1200,675
im=Image.new("RGB",(W,H),(11,18,32)); d=ImageDraw.Draw(im)
for x in range(0,W,40): d.line([(x,0),(x,H)],fill=(17,26,44))
for y in range(0,H,40): d.line([(0,y),(W,y)],fill=(17,26,44))
d.rectangle([0,0,14,H],fill=acc)
f=ImageFont.truetype(B,26); lab="FINTECH SPOTLIGHT"
tw=d.textlength(lab,font=f); d.rectangle([70,70,70+tw+36,120],fill=acc); d.text((88,78),lab,font=f,fill=(11,18,32))
d.text((70+tw+60,82),f"DIY GUIDE #{num}",font=ImageFont.truetype(B,24),fill=(148,163,184))
for size in (60,56,52,48,44,40):
    ft=ImageFont.truetype(B,size); lines=[]; cur=""
    for w in title.split(" "):
        t=(cur+" "+w).strip()
        if d.textlength(t,font=ft)<=W-150: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur)
    if len(lines)*size*1.22<=360: break
y=160
for l in lines: d.text((70,y),l,font=ft,fill=(248,250,252)); y+=int(size*1.22)
d.line([(70,H-95),(W-70,H-95)],fill=(51,65,85),width=2)
d.text((70,H-78),"FINTECH TELEX",font=ImageFont.truetype(B,30),fill=acc)
fr=ImageFont.truetype(R,24); s=f"fintechtelex.com  |  {date}"
d.text((W-70-d.textlength(s,font=fr),H-72),s,font=fr,fill=(148,163,184))
im.save(out); print(len(lines),size)
