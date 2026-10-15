import json,os,sys
SP=sys.argv[1]; W=os.path.join(SP,'work'); C=os.path.join(SP,'chunks'); os.makedirs(C,exist_ok=True)
vals={}
for f in sorted(os.listdir(W)):
    for k,v in json.load(open(os.path.join(W,f),encoding='utf-8')).items():
        vals.setdefault(v,0); vals[v]+=1
u=sorted(vals); print('unique',len(u),'chars',sum(map(len,u)))
# chunks by ~6000 chars
cur=[];n=0;i=0
for v in u:
    cur.append(v); n+=len(v)
    if n>6000 or len(cur)>=250:
        json.dump(cur,open(os.path.join(C,'c%04d.json'%i),'w',encoding='utf-8'),ensure_ascii=False,indent=0); i+=1; cur=[];n=0
if cur: json.dump(cur,open(os.path.join(C,'c%04d.json'%i),'w',encoding='utf-8'),ensure_ascii=False,indent=0); i+=1
print('chunks',i)
