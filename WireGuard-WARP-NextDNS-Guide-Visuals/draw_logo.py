#!/usr/bin/env python3
"""Guide logo: village tree three quarter view, short gnarled trunk, wide low branches,
postcards tied with string, blue borders, brass pins, one central card hanging lower
and square to viewer, blank with a stamp gum square top right. Wordmark in Artifika."""
import sys, math, random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
random.seed(11)
W=H=1024
v=sys.argv[1] if len(sys.argv)>1 else "ship"
BLUE=(38,74,138); CREAM=(246,238,214); GUM=(216,196,140); BROWN=(122,90,58); BRASS=(176,138,62)
img=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(img,"RGBA")
d.ellipse([112,760,912,830],fill=(226,216,188))
# trunk gnarled
d.polygon([(462,790),(492,560),(500,430),(524,560),(556,790)],fill=(96,72,48))
d.line([(500,470),(488,640)],fill=(76,56,36),width=6)
branches=((502,470,180,300),(506,440,360,258),(510,452,660,262),(508,420,850,318),(504,500,300,372),(508,500,730,392))
for bx,by,ex,ey in branches:
    d.line([(bx,by),(ex,ey)],fill=(96,72,48),width=15); d.line([(bx,by),(ex,ey)],fill=(110,84,56),width=6)
for i in range(46):
    bx,by,ex,ey=branches[i%len(branches)]; t=random.random()
    x=int(bx+(ex-bx)*t+random.randint(-18,18)); y=int(by+(ey-by)*t+random.randint(-12,12))
    d.ellipse([x,y,x+20,y+11],fill=(100,128,80) if i%2 else (88,116,70))
# hanging cards
def card(cx,cy,w2=34,h2=46,gum=True):
    d.rectangle([cx-w2,cy,cx+w2,cy+h2],fill=CREAM,outline=BLUE,width=3)
    if gum: d.rectangle([cx+w2-20,cy+6,cx+w2-6,cy+20],fill=GUM)
    d.ellipse([cx-5,cy-9,cx+5,cy+1],fill=BRASS)
for (x,y0,ln) in ((250,300,44),(392,272,58),(660,278,40),(812,330,52),(330,382,36),(716,400,44)):
    cx=x; cy=y0+ln; d.line([(x,y0),(cx,cy)],fill=BROWN,width=3); card(cx,cy,30,40)
# central card lower, square, string detail must survive at 64px
cx,cy=512,470
d.line([(508,428),(cx,cy)],fill=BROWN,width=5 if v!="v1" else 3)
card(cx,cy,58,78,gum=True)
f=ImageFont.truetype("fonts/Artifika.ttf",40)
txt="WireGuard-WARP-NextDNS-Guide"; tw=d.textlength(txt,font=f)
d.text(((W-tw)/2,868),txt,font=f,fill=BLUE)
rng=np.random.default_rng(2); a=np.asarray(img).astype(np.int16); n=rng.normal(0,4,a.shape[:2])[...,None]
img=Image.fromarray(np.clip(a+n,0,255).astype(np.uint8))
out="logo.png" if v=="ship" else f"scratch/logo-{v}.png"
img.save(out); print(out)
img.resize((64,64),Image.LANCZOS).save(f"scratch/logo64-{v}.png"); print("64px saved")
