#!/bin/bash
##########################################################################
# Name: fetchIPlocation.bash
#
# ./fetchIPlocation.bash
#
# Usage: Using curl command to fetch Tor exit node list and search server location with ipinfo.io
#
# Author: Ryosuke Tomita
# Date: 2021/06/19
##########################################################################
function installPackage(){
    if type curl > /dev/null 2>&1; then
        :
    else
        sudo apt install curl
    fi
}

function makeCSV(){
    exitLocationCSV="$(date +'%Y_%m%d_%H%M').csv"
    rm $exitLocationCSV 2>/dev/null
    touch $exitLocationCSV
}

function IPlocate(){
    location=$(curl -s ipinfo.io/$i/loc)
#    if [[ $location ]]; then
    echo -n $location
    echo -n ",${i}"
    echo ""
#    else
#    :
fi
}

# main
installPackage
makeCSV
exitNodeIP=($(curl -s https://check.torproject.org/exit-addresses | grep ExitAddress | cut -d ' ' -f2))

echo "longitude,latitude,IPaddress" | tee -a $exitLocationCSV
for i in ${exitNodeIP[@]};
do
#    curl ipinfo.io/${i}/loc
    IPlocate | tee -a $exitLocationCSV
done

