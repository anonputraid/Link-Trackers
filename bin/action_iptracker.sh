#!/bin/bash
# -*-  Tools Hacking Remix By Ytn4en


ip_tracker(){
    log=$(grep -a 'log' .config.cfg | cut -d '=' -f2)
    ip=$(grep -a 'IP:' $log/ip.txt | cut -d " " -f2 | tr -d '\r')
    iptracker=$(curl -s -L "www.ip-tracker.org/locator/ip-lookup.php?ip=$ip" --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31" > $log/iptracker2.log)
    
}

ip_tracker