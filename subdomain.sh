amass enum -d $1 -json ~/amass_sub_output/$1.json -config ~/c1.ini
mkdir ~/aquatone/$1
python amass2aqua.py $1
