import json,sys,os,re
SP,i=sys.argv[1],sys.argv[2]
P=re.compile(r'%(\d+\$)?[-#+ 0,(]*\d*(\.\d+)?[sdfxXc%]|§.')
s=json.load(open(os.path.join(SP,'chunks',f'c{i}.json'),encoding='utf-8')); t=json.load(open(os.path.join(SP,'t',f'c{i}.json'),encoding='utf-8'))
for j in range(min(len(s),len(t))):
    a=sorted(m.group(0) for m in P.finditer(s[j])); b=sorted(m.group(0) for m in P.finditer(t[j]))
    if a!=b: print(j,repr(s[j]),'|',repr(t[j]),'| next src',repr(s[j+1]) if j+1<len(s) else ''); break
