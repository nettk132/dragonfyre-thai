import json,os,sys,zipfile
SP=sys.argv[1]; OUT=sys.argv[2]
# Thai font size / vertical shift (bigger shift = lower). Override: build.py SP OUT SIZE SHIFT
TH_SIZE=float(sys.argv[3]) if len(sys.argv)>3 else 12.0
TH_SHIFT=float(sys.argv[4]) if len(sys.argv)>4 else 0.1
m={}
for f in os.listdir(os.path.join(SP,'t')):
    s=json.load(open(os.path.join(SP,'chunks',f),encoding='utf-8')); t=json.load(open(os.path.join(SP,'t',f),encoding='utf-8'))
    if len(s)==len(t): m.update(zip(s,t))
z=zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED); n=tot=0
z.writestr('pack.mcmeta',json.dumps({"pack":{"pack_format":15,"description":"แปลไทย Dragonfyre"}},ensure_ascii=False))
F=os.path.join(SP,'font')
z.write(os.path.join(F,'thai.ttf'),'assets/thaifix/font/thai.ttf'); z.write(os.path.join(F,'OFL.txt'),'FONT_LICENSE_OFL.txt')
fd={"providers":[{"type":"reference","id":"minecraft:include/space"},{"type":"reference","id":"minecraft:include/default"},
 {"type":"ttf","file":"thaifix:thai.ttf","size":TH_SIZE,"oversample":4.0,"shift":[0,TH_SHIFT],"skip":""},{"type":"reference","id":"minecraft:include/unifont"}]}
z.writestr('assets/minecraft/font/default.json',json.dumps(fd))
TT={"providers":[{"type":"ttf","file":"thaifix:thai.ttf","size":TH_SIZE,"oversample":4.0,"shift":[0,TH_SHIFT],"skip":""}]}
# Thai TTF ahead of unifont in every font that references it (other packs' default.json, Force Unicode, uniform)
z.writestr('assets/minecraft/font/include/unifont.json',json.dumps(TT))
z.writestr('assets/minecraft/font/uniform.json',json.dumps(TT))
W=os.path.join(SP,'work')
for f in os.listdir(W):
    d=json.load(open(os.path.join(W,f),encoding='utf-8')); import re
    NAME=re.compile(open(os.path.join(SP,'namekey.txt')).read())
    o={k:m[v] for k,v in d.items() if v in m and not NAME.match(k)}
    tot+=len(d); n+=len(o)
    if o: z.writestr(f'assets/{f[:-5]}/lang/th_th.json',json.dumps(o,ensure_ascii=False,indent=1))
z.close(); print(f'translated {n}/{tot}')
