#!/usr/bin/env python3
"""Guide banner: village square morning, postcard tree left, post office right with
brass date stamp on ink pad, blue pigeonholes, clerk hand sliding a card, bicycle with
empty leather post bag, stepladder, basket on bench, long cream notice board on the
office wall lettered in Artifika with the repo title among smaller blank notices."""
import sys, random, math
from PIL import Image, ImageDraw, ImageFont
import numpy as np
random.seed(29)
W,H=1600,900
v=sys.argv[1] if len(sys.argv)>1 else "ship"
BLUE=(38,74,138); CREAM=(246,238,214); GUM=(216,196,140); BROWN=(122,90,58); BRASS=(176,138,62)
img=Image.new("RGB",(W,H),(208,212,214)); d=ImageDraw.Draw(img,"RGBA")
# cobbles
d.rectangle([0,560,W,900],fill=(178,168,154))
for row in range(7):
    y=580+row*46
    for cx in range(-1,14):
        x=cx*130+(row%2)*60+random.randint(-8,8); d.ellipse([x,y,x+104,y+30],outline=(146,136,120),width=2,fill=(186,176,162))
# post office right
d.rectangle([880,220,1560,580],fill=(228,220,200)); d.rectangle([880,220,1560,276],fill=BLUE)
d.rectangle([1150,320,1500,540],fill=(196,186,164))
for gx in range(7):
    for gy in range(5): d.rectangle([1166+gx*46,336+gy*39,1202+gx*46,364+gy*39],outline=BLUE,width=3,fill=(88,110,150))
# counter window with date stamp and clerk hand sliding a card
d.rectangle([910,330,1120,520],fill=(240,234,216),outline=(120,100,70),width=4)
d.ellipse([948,452,1010,478],fill=(90,70,50)); d.rectangle([968,420,990,456],fill=BRASS)  # date stamp on ink pad
d.rectangle([952,486,1014,502],fill=(40,40,48))
d.rectangle([1018,392,1096,438],fill=CREAM,outline=BLUE,width=2)  # card being slid
d.polygon([(1096,398),(1140,404),(1140,430),(1096,434)],fill=(222,186,152))  # wrist and hand
# notice board on office wall with title among blank notices
d.rectangle([900,600,1540,760],fill=CREAM,outline=BROWN,width=5)
for nx,ny in ((916,616),(1524,616),(916,744),(1524,744)): d.ellipse([nx-5,ny-5,nx+5,ny+5],fill=BRASS)
f=ImageFont.truetype("fonts/Artifika.ttf",33 if v!="v1" else 44)
txt="WireGuard-WARP-NextDNS-Guide"; tw=d.textlength(txt,font=f)
d.text(((1220-tw/2),636),txt,font=f,fill=BLUE)
for bx,by,bw in ((940,700,150),(1330,700,170),(1130,700,120)):
    d.rectangle([bx,by,bx+bw,by+34],fill=(240,234,218),outline=BLUE,width=2)
# tree left
d.polygon([(330,880),(362,520),(378,360),(398,520),(430,880)],fill=(96,72,48))
branches=((372,420,90,270),(376,392,220,232),(380,410,540,246),(378,372,650,300),(374,470,160,330))
for bx,by,ex,ey in branches: d.line([(bx,by),(ex,ey)],fill=(96,72,48),width=15); d.line([(bx,by),(ex,ey)],fill=(110,84,56),width=6)
for i in range(60):
    bx,by,ex,ey=branches[i%len(branches)]; t=random.random()
    x=int(bx+(ex-bx)*t+random.randint(-20,20)); y=int(by+(ey-by)*t+random.randint(-14,14))
    d.ellipse([x,y,x+23,y+12],fill=(100,128,80) if i%2 else (88,116,70))
for (x,y0,ln) in ((150,282,40),(268,250,54),(520,262,44),(620,312,38),(210,344,48),(470,300,60)):
    cy=y0+ln; d.line([(x,y0),(x,cy)],fill=BROWN,width=2)
    d.rectangle([x-27,cy,x+27,cy+38],fill=GUM if x%3==0 else CREAM,outline=BLUE,width=2)
    d.ellipse([x-4,cy-8,x+4,cy],fill=BRASS)
# bench circle (front arc), ladder, basket
d.rectangle([190,724,560,754],fill=(128,96,60)); d.rectangle([214,754,242,824],fill=(106,78,46)); d.rectangle([508,754,536,824],fill=(106,78,46))
for t in range(5): d.line([(596,600+t*4),(690,600+t*48)],fill=(140,108,66),width=0)  # no-op keeps ladder code local
for i in range(5):
    y=566+i*52; d.line([(606+i*3,y),(700-i*2,y)],fill=(140,108,66),width=6)
d.line([(606,566),(622,826)],fill=(140,108,66),width=8); d.line([(700,566),(692,826)],fill=(140,108,66),width=8)
d.polygon([(96,700),(200,700),(186,756),(110,756)],fill=(150,116,72))
for bx,by in ((126,688),(160,684)): d.ellipse([bx-14,by-12,bx+14,by+12],outline=BROWN,width=3,fill=(226,206,170))
# bicycle at office step with empty post bag
for wx,wy in ((1180,800),(1330,800)):
    d.ellipse([wx-36,wy-36,wx+36,wy+36],outline=(52,52,56),width=5)
d.line([(1180,800),(1240,724),(1330,800),(1262,800),(1216,724)],fill=(52,52,56),width=5)
d.line([(1216,724),(1270,724)],fill=(52,52,56),width=5)
d.rectangle([1296,742,1352,782],fill=(130,92,58))  # leather post bag, empty
rng=np.random.default_rng(8); a=np.asarray(img).astype(np.int16); n=rng.normal(0,4,a.shape[:2])[...,None]
img=Image.fromarray(np.clip(a+n,0,255).astype(np.uint8))
out="banner.png" if v=="ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
