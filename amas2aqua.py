import json,sys
domain=sys.argv[1]
fwt=open('/Users/sam-8402/aquatone/'+domain+'/hosts.txt','w')
fwj=open('/Users/sam-8402/aquatone/'+domain+'/hosts.json','w')

f=open('/Users/sam-8402/Desktop/sample/'+domain+'.json','r').read().split('\n')[:-1]
list2json = {}
for jsonData in f:
    jData=json.loads(jsonData)
    ips=jData['addresses']
    for ip in ips:
        fwt.write(jData['name']+','+ip['ip']+'\n')
        list2json[jData['name']]=ip['ip']
fwj.write(json.dumps(list2json))
