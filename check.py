import json,os,sys,re
SP=sys.argv[1]; ids=sys.argv[2:]
P=re.compile(r'%(\d+\$)?[-#+0,(]*\d*(\.\d+)?[sdfxXc%]|\{[^}]*\}|§.|\n|\n|<[^>]+>|\$\([^)]*\)')
for i in ids:
    s=json.load(open(os.path.join(SP,'chunks',f'c{i}.json'),encoding='utf-8'))
    t=json.load(open(os.path.join(SP,'t',f'c{i}.json'),encoding='utf-8'))
    if len(s)!=len(t): print(i,'LEN',len(s),len(t)); continue
    Q=re.compile(r'%[-#+0,(]*\d*(\.\d+)?[sdfxXc]')
    bad=[j for j,(a,b) in enumerate(zip(s,t)) if [m.group(0) for m in Q.finditer(a.replace('%%',''))]!=[m.group(0) for m in Q.finditer(b.replace('%%',''))]]+[j for j,(a,b) in enumerate(zip(s,t)) if sorted(m.group(0) for m in P.finditer(a))!=sorted(m.group(0) for m in P.finditer(b))]
    print(i,'ok' if not bad else 'bad '+str([(j,s[j][:60],t[j][:60]) for j in bad[:8]]))
