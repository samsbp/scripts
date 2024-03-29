import json,os,subprocess,time,requests,argparse

parser = argparse.ArgumentParser(description='Script for integrating amass and gobuster into')
parser.add_argument("-d","--domains", help="domains",required=True)
args = parser.parse_args()
domains=args.domains.split(',')
global_ips=[]
global_hosts={}
for domain in domains:

    # f=open('/root/amass_sub_output'+domain+'.json','r').read()
    # data=f.split('\n')[:-1]
    # host={}
    # ipList={}
    # for d in data:
    #     j=json.loads(d)
    #     subdomain = j['name']
    #     subdomain_ip=[]
    #
    #     portList=[]
    #     host[subdomain]={}
    #     print 'collecting ports for '+subdomain
    #     for ip in j['addresses']:
    #         ip_address=ip['ip']
    #         if(':' not in ip_address):
    #             subdomain_ip.append(ip_address)
    #
    #
    #             print ip_address
    #             #print 'curl https://www.shodan.io/host/'+ip_address+" | grep \"<div class=\\\"port\\\">\" | sed 's/<div class=\"port\">//g' | sed 's@</div>@@g'"
    #             if(ip_address not in global_ips):
    #                 ports=subprocess.check_output("curl -s https://www.shodan.io/host/"+ip_address+" | grep \"<div class=\\\"port\\\">\" | sed 's/<div class=\"port\">//g' | sed 's@</div>@@g'",shell=True)
    #                 ports=ports.split('\n')[:-1]
    #                 global_ips.append(ip_address)
    #                 global_hosts[ip_address]=ports
    #                 time.sleep(1)
    #                 #print ports,'\n'
    #
    #                 ipList[ip_address]=ports
    #             else:
    #                 print "ports are already computed"
    #                 ports=ipList[ip_address]
    #             portList+=ports
    #
    #     host[subdomain]['ips']=subdomain_ip
    #     host[subdomain]['ports']=list(set(portList))
    #     print host[subdomain]['ports'],"\n"
    # host['ip_ports']=ipList
    #
    # for d in data:
    #     j=json.loads(d)
    #     subdomain = j['name']
    #     ports=host[subdomain]['ports']
    #     for port in ports:
    #         print "trying "+subdomain+":"+port
    #         try:
    #             url="http://"+subdomain+":"+port
    #             req_http=requests.head(url,verify=False,timeout=5)
    #
    #             if(req_http.status_code==400):
    #                 url="https://"+subdomain+":"+port
    #                 req_https=requests.head(url,timeout=5)
    #                 if(req_https.status_code==400):
    #                     break
    #             print "gobuster: "+url
    #             print subprocess.check_output("gobuster dir -u "+url+" -w common_quick.txt -t 250 -k --timeout=10s -s 200,301,403 -o /root/amass_buster_output/"+domain,shell=True)
    #             #go_out=open('/root/amass_buster_output/'+domain).read()
	# 	print "sending data to recon"
    #             subprocess.check_output('./slackmsg.sh '+domain+' '+url)
    #
    #         except:
    #             continue

    aquatone_ips=[]
    aquatone_hosts=[]
    ip_ports={}
    aquatone_f=open('/root/aquatone/'+domain+'/hosts.txt','r').read()
    aquatone_data=aquatone_f.split('\n')[:-1]
    for data in aquatone_data:
        data_split = data.split(',')
        ip_address = data_split[1]
        if(ip_address in global_ips):
            ip_ports[ip_address]=global_hosts[ip_address]
            print 'aldready computed for ',ip_address
            continue
        else:
            global_ips.append(ip_address)
            ports=subprocess.check_output("curl -s https://www.shodan.io/host/"+ip_address+" | grep \"<div class=\\\"port\\\">\" | sed 's/<div class=\"port\">//g' | sed 's@</div>@@g'",shell=True)
            ports=ports.split('\n')[:-1]
            print ip_address,ports
            global_hosts[ip_address]=ports
            ip_ports[ip_address]=ports
            time.sleep(1)

    for data in aquatone_data:
        data_split = data.split(',')
        ip_address = data_split[1]
        subdomain= data_split[0]

        for port in ip_ports[ip_address]:
            print "trying "+subdomain+":"+port
            try:
                url="http://"+subdomain+":"+port
                req_http=requests.head(url,verify=False,timeout=5)

                if(req_http.status_code==400):
                    url="https://"+subdomain+":"+port
                    req_https=requests.head(url,timeout=5)
                    if(req_https.status_code==400):
                        break
                print "gobuster: "+url
                print subprocess.check_output("gobuster dir -u "+url+" -w common_quick.txt -t 250 -k --timeout=10s -s 200,301,403 -o /root/amass_buster_output/"+domain,shell=True)
                #go_out=open('/root/amass_buster_output/'+domain).read()
		print "sending data to recon"
                subprocess.check_output('./slackmsg.sh '+domain+' '+url)

            except:
                continue

    aquatone_ips=[]
    aquatone_hosts=[]
    ip_ports={}
    aquatone_f=open('data/'+domain+'_hosts.txt','r').read()
    aquatone_data=aquatone_f.split('\n')[:-1]
    for data in aquatone_data:
        data_split = data.split(',')
        ip_address = data_split[1]
        if(ip_address in global_ips):
            ip_ports[ip_address]=global_hosts[ip_address]
            print 'aldready computed for ',ip_address
            continue
        else:
            global_ips.append(ip_address)

            ports=subprocess.check_output("curl -s https://www.shodan.io/host/"+ip_address+" | grep \"<div class=\\\"port\\\">\" | sed 's/<div class=\"port\">//g' | sed 's@</div>@@g'",shell=True)
            ports=ports.split('\n')[:-1]
            print ip_address,ports
            global_hosts[ip_address]=ports
            ip_ports[ip_address]=ports
            time.sleep(1)

    for data in aquatone_data:
        data_split = data.split(',')
        ip_address = data_split[1]
        subdomain= data_split[0]

        for port in ip_ports[ip_address]:
            print "trying "+subdomain+":"+port
            try:
                url="http://"+subdomain+":"+port
                req_http=requests.head(url,verify=False,timeout=5)

                if(req_http.status_code==400):
                    url="https://"+subdomain+":"+port
                    req_https=requests.head(url,timeout=5)
                    if(req_https.status_code==400):
                        break
                print "gobuster: "+url
                print subprocess.check_output("gobuster dir -u "+url+" -w common_quick.txt -t 250 -k --timeout=10s -s 200,301,403 -o /root/amass_buster_output/"+domain,shell=True)
                #go_out=open('/root/amass_buster_output/'+domain).read()
		print "sending data to recon"
                subprocess.check_output('./slackmsg.sh '+domain+' '+url)

            except:
                continue

