echo "subdomain enumeration [$1]"
#amass enum -d $1 -json ~/amass_sub_output/$1.json -config ~/c1.ini
mkdir ~/aquatone/$1
python amass2aqua.py $1
echo "takeover testing [$1]"
aquatone-takeover -d $1
echo "sending data to slack[#recon]"
msg="$(cat ~/aquatone/starbucks.com/takeovers.json)"
slackcli -h "recon" -t $SLACK_TOKEN -u "script" -m "$msg"

