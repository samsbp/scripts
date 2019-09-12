import sys,json,subprocess
f=open(sys.argv[1],'r').read()
out_json=open('/root/aquatone/'+sys.argv[2]+'/hosts.json','w')
out_txt=open('/root/aquatone/'+sys.argv[2]+'/hosts.txt','w')
res_txt=''
res_json={}
f=f.split('\n')[:-1]
#print f
for line in f:
    res=line.split(' ')
    res[0]=res[0][:-1]
    if(res[0][0]=='*'):
        res[0]='awedvaf123213afadsf'+res[0][1:]
        print res[0]
    ip=subprocess.check_output('dig +short '+res[0]+' | tail -n1',shell=True).replace('\n','')
    res_txt+=res[0]+','+ip+'\n'
    res_json[res[0]]=ip 
print res_json
out_json.write(json.dumps(res_json))
out_txt.write(res_txt)

