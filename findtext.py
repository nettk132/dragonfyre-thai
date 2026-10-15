# usage: python findtext.py <modpack folder> "<english phrase>"
# searches loose files and files inside .jar/.zip for the phrase, prints where it lives
import os, sys, zipfile
D=sys.argv[1]; Q=sys.argv[2].encode('utf-8')
EXT=('.json','.json5','.toml','.js','.snbt','.txt','.lang','.cfg','.yml','.yaml','.properties','.mcfunction','.nbt')
for root,_,files in os.walk(D):
    for f in files:
        p=os.path.join(root,f); lf=f.lower()
        try:
            if lf.endswith(('.jar','.zip')):
                with zipfile.ZipFile(p) as z:
                    for n in z.namelist():
                        if n.lower().endswith(EXT) and Q in z.read(n): print(p,'->',n)
            elif lf.endswith(EXT):
                if Q in open(p,'rb').read(): print(p)
        except Exception: pass
