msg_200="$(cat /root/amass_buster_output/$1 | grep '200)')"
slackcli -h "recon_200" -t $SLACK_TOKEN -u "$2[200]" -m "$msg_200"
msg_301="$(cat /root/amass_buster_output/$1 | grep '301)')"
slackcli -h "recon_300" -t $SLACK_TOKEN -u "$2[301]" -m "$msg_301"
msg_403="$(cat /root/amass_buster_output/$1 | grep '403)')"
slackcli -h "recon_403" -t $SLACK_TOKEN -u "$2[403]" -m "$msg_403"
