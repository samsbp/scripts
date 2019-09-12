import sys,json,subprocess
f=open(sys.argv[1],'r').read()
out=open(sys.argv[2],'w')
res_txt=''
f=f.split('\n')[:-1]
#print f
for line in f:
    res=line.split(' ')
    res[0]=res[0][:-1]
    ip=res[2]
    res_txt+=res[0]+','+ip+'\n'
out.write(res_txt)
