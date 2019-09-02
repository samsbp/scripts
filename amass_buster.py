import json,os,subprocess,time,requests,argparse

parser = argparse.ArgumentParser(description='Script for integrating amass and gobuster into')
parser.add_argument("-d","--domains", help="domains",required=True)
args = parser.parse_args()
domain=args.domains
f=open('/Users/sam-8402/Desktop/sample/'+domain+'.json','r').read()
data=f.split('\n')[:-1]
host={}
ipList={}
for d in data:
    j=json.loads(d)
    subdomain = j['name']
    subdomain_ip=[]

    portList=[]
    host[subdomain]={}
    print 'collecting ports for '+subdomain
    for ip in j['addresses']:
        ip_address=ip['ip']
        if(':' not in ip_address):
            subdomain_ip.append(ip_address)


            print ip_address
            #print 'curl https://www.shodan.io/host/'+ip_address+" | grep \"<div class=\\\"port\\\">\" | sed 's/<div class=\"port\">//g' | sed 's@</div>@@g'"
            if(ip_address not in ipList.keys()):
                ports=subprocess.check_output("curl -s https://www.shodan.io/host/"+ip_address+" | grep \"<div class=\\\"port\\\">\" | sed 's/<div class=\"port\">//g' | sed 's@</div>@@g'",shell=True)
                ports=ports.split('\n')[:-1]
                time.sleep(1)
                #print ports,'\n'

                ipList[ip_address]=ports
            else:
                print "ports are already computed"
                ports=ipList[ip_address]
            portList+=ports

    host[subdomain]['ips']=subdomain_ip
    host[subdomain]['ports']=list(set(portList))
    print host[subdomain]['ports'],"\n"
host['ip_ports']=ipList

for d in data:
    j=json.loads(d)
    subdomain = j['name']
    ports=host[subdomain]['ports']
    for port in ports:
        url="http://"+subdomain+":"+port
        req_http=requests.head(url,verify=False)

        if(req_http.status_code==400):
            url="https://"+subdomain+":"+port
            req_https=requests.head(url)
            if(req_https.status_code==400):
                break
        print url
        try:
            print "gobuster: "+url
            print subprocess.check_output("gobuster dir -u "+url+" -w common_quick.txt -t 50 -k --timeout=10s -s 200,301",shell=True)
        except:
            continue
