import zipfile, json, os, sys, glob, re
D=sys.argv[1]; OUT=sys.argv[2]
def load(b):
    t=b.decode('utf-8-sig','replace')
    try: return json.loads(t)
    except: 
        try: return json.loads(re.sub(r',\s*}', '}', re.sub(r'^\s*//.*$','',t,flags=re.M)))
        except: return None
en={}; th={}
for jar in glob.glob(os.path.join(glob.escape(D),'mods','*.jar')):
    try: z=zipfile.ZipFile(jar)
    except: continue
    for n in z.namelist():
        m=re.match(r'assets/([^/]+)/lang/(en_us|th_th)\.json$',n,re.I)
        if m:
            d=load(z.read(n))
            if not isinstance(d,dict): continue
            tgt=en if m.group(2).lower()=='en_us' else th
            tgt.setdefault(m.group(1),{}).update({k:v for k,v in d.items() if isinstance(v,str)})
for ns,d in en.items():
    rest={k:v for k,v in d.items() if k not in th.get(ns,{}) and v.strip()}
    if rest: json.dump(rest,open(os.path.join(OUT,ns+'.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=0)
tot=sum(len(json.load(open(os.path.join(OUT,f),encoding='utf-8'))) for f in os.listdir(OUT))
chars=sum(sum(len(v) for v in json.load(open(os.path.join(OUT,f),encoding='utf-8')).values()) for f in os.listdir(OUT))
print('namespaces',len(os.listdir(OUT)),'entries',tot,'chars',chars,'already_th',sum(len(v) for v in th.values()))
