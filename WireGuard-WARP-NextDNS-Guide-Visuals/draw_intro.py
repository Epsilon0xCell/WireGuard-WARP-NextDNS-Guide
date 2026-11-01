#!/usr/bin/env python3
"""Guide intro: postcard tree in a quiet square, wordless. Cobbles, fallen card face
down, bench circling trunk, basket of string pins and blank cards, cards hanging by
string from every limb, stepladder, post office with dark window and pigeonhole grid,
house fronts, well, road leaving between buildings to hills. No text of any kind."""
import sys, random, math
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(23)
W,H=1600,900
v=sys.argv[1] if len(sys.argv)>1 else "ship"
BLUE=(38,74,138); CREAM=(246,238,214); GUM=(216,196,140); BROWN=(122,90,58); BRASS=(176,138,62)
img=Image.new("RGB",(W,H),(214,206,188)); d=ImageDraw.Draw(img,"RGBA")
# sky strip and hills, road leaving
d.rectangle([0,0,W,300],fill=(206,214,220))
d.polygon([(0,300),(500,210),(760,300)],fill=(168,176,158)); d.polygon([(860,300),(1180,200),(1600,300)],fill=(158,168,150))
d.polygon([(748,300),(852,300),(872,470),(728,470)],fill=(196,188,170))
# house fronts left, shutters closed
for hx,hw,col in ((40,300,(196,178,158)),(360,180,(186,172,166))):
    d.rectangle([hx,300,hx+hw,560],fill=col)
    for sx in (hx+36,hx+hw-96):
        d.rectangle([sx,350,sx+58,440],fill=(120,116,104)); d.line([(sx+29,350),(sx+29,440)],fill=(90,86,78),width=3)
# well left foreground-mid
d.rectangle([120,560,260,640],fill=(150,146,138)); d.rectangle([104,544,276,566],fill=(128,124,116))
d.polygon([(100,544),(190,492),(280,544)],fill=(110,88,64))
d.rectangle([168,566,214,600],fill=(90,90,96),outline=(60,60,64),width=2)
# post office right: counter window dark, pigeonhole grid inside
d.rectangle([1120,280,1560,580],fill=(226,218,198)); d.rectangle([1120,280,1560,330],fill=BLUE)
d.rectangle([1330,360,1520,540],fill=(52,54,60))
for gx in range(6):
    for gy in range(5):
        d.rectangle([1344+gx*28,374+gy*31,1366+gx*28,398+gy*31],outline=BLUE,width=2,fill=(70,84,110))
d.rectangle([1150,380,1300,540],fill=(196,186,164))
# road leaving the square through a gap in the buildings, narrowing to hills
d.polygon([(566,470),(646,470),(622,300),(590,300)],fill=(206,198,178))
d.polygon([(590,300),(622,300),(640,238),(574,238)],fill=(198,204,190))
# cobbles foreground
d.rectangle([0,580,W,900],fill=(178,168,154))
for row in range(7):
    y=600+row*44
    for cx in range(-1,14):
        x=cx*130+(row%2)*60+random.randint(-8,8)
        d.ellipse([x,y,x+104,y+30],outline=(146,136,120),width=2,fill=(186,176,162))
# tree centre: trunk, branches spreading to both edges
d.polygon([(742,900),(782,560),(806,380),(826,560),(858,900)],fill=(96,72,48))
for bx,by,ex,ey in ((790,430,300,268),(800,400,560,238),(806,420,1080,250),(798,380,1300,300),(794,470,420,330),(802,470,1180,360)):
    d.line([(bx,by),(ex,ey)],fill=(96,72,48),width=16)
    d.line([(bx,by),(ex,ey)],fill=(110,84,56),width=7)
# leaves clustered along the branch lines
branches=((790,430,300,268),(800,400,560,238),(806,420,1080,250),(798,380,1300,300),(794,470,420,330),(802,470,1180,360))
for i in range(110):
    bx,by,ex,ey=branches[i%len(branches)]; t=random.random()
    x=int(bx+(ex-bx)*t+random.randint(-26,26)); y=int(by+(ey-by)*t+random.randint(-18,18))
    d.ellipse([x,y,x+24,y+13],fill=(104,132,84) if i%2 else (92,120,74))
# hanging cards by string, cream and gum rectangles with blue borders, no writing
cards=[]
for i in range(26):
    x=random.randint(300,1300); y0=random.randint(240,380); ln=random.randint(28,74); ang=random.randint(-9,9)
    cx=x+int(math.sin(math.radians(ang))*ln); cy=y0+ln
    d.line([(x,y0),(cx,cy)],fill=BROWN,width=2)
    w2,h2=30,21
    gum = i%4==0
    d.rectangle([cx-w2,cy,cx+w2,cy+h2*2],fill=GUM if gum else CREAM,outline=BLUE,width=2)
    cards.append((cx,cy))
# bench circling trunk + basket with string balls, pins heap, blank card bundle
d.rectangle([600,742,1000,772],fill=(128,96,60)); d.rectangle([620,772,650,842],fill=(106,78,46)); d.rectangle([950,772,980,842],fill=(106,78,46))
d.polygon([(1052,742),(1180,742),(1158,806),(1074,806)],fill=(150,116,72))
for bx,by in ((1086,730),(1124,726),(1106,742)): d.ellipse([bx-15,by-13,bx+15,by+13],outline=BROWN,width=3,fill=(226,206,170))
for i in range(8):
    px=1148+random.randint(0,26); py=752+random.randint(0,14); d.ellipse([px,py,px+6,py+6],fill=BRASS)
d.rectangle([520,712,592,758],fill=CREAM,outline=BLUE,width=2); d.line([(520,735),(592,735)],fill=BROWN,width=2)
# stepladder right of trunk
for t in range(5):
    y=560+t*52; d.line([(1212+t*4,y),(1310-t*2,y)],fill=(140,108,66),width=7)
d.line([(1212,560),(1232,816)],fill=(140,108,66),width=9); d.line([(1310,560),(1300,816)],fill=(140,108,66),width=9)
# fallen card face down bottom left with trailing string
d.rectangle([120,792,232,852],fill=(232,220,190),outline=BLUE,width=2)
pts=[(232+int(18*math.sin(k/4)),838-int(k*1.1)) for k in range(14)]; d.line(pts,fill=BROWN,width=2)
# branch shadows striping ground
lay=Image.new("RGBA",(W,H),(0,0,0,0)); ld=ImageDraw.Draw(lay)
for i in range(7): ld.polygon([(300+i*160,600),(380+i*160,600),(240+i*160,900),(120+i*160,900)],fill=(80,80,70,26))
img=Image.alpha_composite(img.convert("RGBA"),lay.filter(ImageFilter.GaussianBlur(6))).convert("RGB")
rng=np.random.default_rng(6); a=np.asarray(img).astype(np.int16); n=rng.normal(0,4,a.shape[:2])[...,None]
img=Image.fromarray(np.clip(a+n,0,255).astype(np.uint8))
out="intro-banner.png" if v=="ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
