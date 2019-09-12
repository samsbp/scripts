echo "subdomain enumeration [$1]"
amass enum -d $1 -json ~/amass_sub_output/$1.json -config ~/c1.ini -o data/$1_amass.txt
/root/tools/findomain-linux -t $1 -o txt
/root/massdns/scripts/subbrute.py  /root/tools/SecLists/Discovery/DNS/dns-Jhaddix.txt $1 > data/$1_subrute.txt
cat $1* data/$1* | uniq | /root/massdns/bin/massdns -r /root/massdns/lists/resolvers.txt -t A -o S -w data/$1_sub_domains.list

mkdir ~/aquatone/$1
python amass2aqua.py $1
echo "takeover testing [$1]"
aquatone-takeover -d $1
echo "sending data to slack[#recon]"
msg="$(cat ~/aquatone/starbucks.com/takeovers.json)"
slackcli -h "recon" -t $SLACK_TOKEN -u "takeovers" -m "$msg"
echo "collecting ports and busting [$1]"
python amass_buster.py -d $1
