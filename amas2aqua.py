import json,sys
domain=sys.argv[1]
fwt=open('~/aquatone/'+domain+'/hosts.txt','w')
fwj=open('~/aquatone/'+domain+'/hosts.json','w')

f=open('~/amass_sub_output/'+domain+'.json','r').read().split('\n')[:-1]
list2json = {}
for jsonData in f:
    jData=json.loads(jsonData)
    ips=jData['addresses']
    for ip in ips:
        fwt.write(jData['name']+','+ip['ip']+'\n')
        list2json[jData['name']]=ip['ip']
fwj.write(json.dumps(list2json))
