#!/usr/bin/python3
import os as console
import subprocess as system
import sys
from configparser import ConfigParser 
from colorama import Fore, Back, Style

Config = {}

class main_controller:
    def initialize(require):
        global Config
        if console.path.isfile(require):
            Config = ConfigParser()
            Config.read(require)
            Config["include"] = { 
                'log' : Config.get('require','log'),
                'banner' : Config.get('require','banner'),
                'root': Config.get('require','home'),
                'bin': Config.get('require','bin')
            }
            return True

    initialize(console.path.join(console.path.dirname(console.path.realpath(__file__))) + "/.config.cfg")
    Log = Config["include"]["log"]
    f = True
    while f:
        if console.path.isfile(Log + "/ip.txt"):
            f = False
            pass 


class track_record:
    def catch_ip():
        global ip_found
        home = Config["include"]["root"]
        Log = Config["include"]["log"] + "/ip.txt"
        ip_found = str(system.check_output("grep -a 'IP:' {} | cut -d ' ' -f2 | tr -d '\r'".format(Log), shell=True) , 'utf-8')
        User_Agent = str(system.check_output("grep -a 'User-Agent:' {}".format(Log), shell=True) , 'utf-8')
        # User_Agent = User_Agent.replace(' User-Agent:', '')
        # print("Victim IP : {}".format(ip_found.replace('IP: ', '')))
        print("")
        sys.stdout.write(Fore.BLUE + "[*] Ip Found !\n")
        sys.stdout.write("[*] Target Ip : {}".format(ip_found))
        sys.stdout.write("[*] User-Agent: {}".format(User_Agent.replace(' User-Agent: ', '')))
        sys.stdout.write("[*] Saved : {}/log/ip.txt\n".format(home))
        pass
    
    def ip_tracker():
        Log = Config["include"]["log"]
        if ip_found != "":
            console.chdir(Log)
            out = str(system.check_output("curl -s -L ipinfo.io/{} ".format(ip_found), shell=True) , 'utf-8')
            console.system('')
            with open('iptracker.log','w') as f:
                for line in out:
                    f.write(line)
        print("")
        sys.stdout.write("[*] Hostname : {}".format(ip_found))
        pass

    def adjective():
        console.chdir(Config["include"]["bin"])
        system.run(["bash","action_iptracker.sh"])
        list_track = ["continent","country","State", "city" , "org" , "AS Number" , "IP Address","loc", "timezone","Ip Currency"]
        for x in list_track:
            console.chdir(Config["include"]["log"])
            f = '"'
            opt = str(system.check_output(
                "grep -o '{}.*' iptracker.log | cut -d '{}' -f3".format(x,f) , shell=True) , 'utf-8')
            if  x == "continent":
                continent = str(system.check_output(
                    "grep -o 'Continent.*' iptracker2.log | head -n1 | cut -d '>' -f3 | cut -d '<' -f1" , shell=True) , 'utf-8')
                if continent != "":
                    sys.stdout.write("[*] Ip Continent :{}".format(continent))
                pass
            elif x == "country":
                country = str(system.check_output(
                    "grep -o 'Country:.*' iptracker2.log | cut -d '>' -f3 | cut -d '&' -f1" , shell=True) , 'utf-8')
                if country != "":
                    sys.stdout.write("[*] Ip Country :{}".format(country))
            
            elif x == "State":
                State = str(system.check_output(
                    "grep -o 'tracking lessimpt.*' iptracker2.log | cut -d '<' -f1 | cut -d '>' -f2" , shell=True) , 'utf-8')
                if State != "":
                    sys.stdout.write("[*] State : {}".format(State))
            elif x == "city":
                f = '"'
                x = 'region'
                region = str(system.check_output(
                    "grep -o '{}.*' iptracker.log | cut -d '{}' -f3".format(x,f) , shell=True) , 'utf-8')
                cutstr = region.replace("\n",'')
                sys.stdout.write("\r[*] City Location : {},{}".format(cutstr,opt))

            elif x == "org":
                ISP = str(system.check_output(
                    "grep -o 'ISP:.*' iptracker2.log | cut -d '<' -f3 | cut -d '>' -f2" , shell=True) , 'utf-8') 
                if ISP != "":
                    sys.stdout.write("[*] ISP : {}".format(ISP))
                else:
                    sys.stdout.write("[*] ISP : {}".format(opt))
            elif x == "AS Number":
                AS_Number = str(system.check_output(
                    "grep -o 'AS Number:.*' iptracker2.log | cut -d '<' -f3 | cut -d '>' -f2" , shell=True) , 'utf-8')                
                rmspace = AS_Number.replace("\n","")
                if AS_Number != "":
                    print("[*] AS Number : {}".format(rmspace))


            elif x == "IP Address":
                IP_Address = str(system.check_output(
                    "grep -o 'IP Address Speed:.*' iptracker2.log | cut -d '<' -f3 | cut -d '>' -f2" , shell=True) , 'utf-8')                 
                if IP_Address != "":
                    sys.stdout.write("[*] Ip Address Speed : {}".format(IP_Address))
            elif x == "loc":
                sys.stdout.write("[*] IP GeoLocation : {}".format(opt))                

            elif x == "timezone":
                sys.stdout.write("[*] IP TimeZone : {}".format(opt))

            elif x == "Ip Currency":
                IP_currency = str(system.check_output(
                    "grep -o 'IP Currency:.*' iptracker2.log | cut -d '<' -f3 | cut -d '>' -f2" , shell=True) , 'utf-8')
                if IP_currency != "":
                    print("[*] IP Currency : {}".format(IP_currency))

        
        console.chdir(Config["include"]["log"])
        if console.path.isfile("iptracker2.log"):
            print("")
            print(Fore.GREEN + "Domain database !" + Style.RESET_ALL)
            print(Fore.BLUE)
            Whois_tools = str(system.check_output(
                "whois {}".format(ip_found) , shell=True) , 'utf-8')
            del_lines1 = Whois_tools.replace("% [whois.apnic.net]","")
            del_lines2 = del_lines1.replace("% Whois data copyright terms    http://www.apnic.net/db/dbcopyright.html", "")
            print("\n" + del_lines2.strip("\n"))
            console.chdir(Config["include"]["log"])
            console.system("rm *")
            console.system("killall ngrok")
        pass

       

    catch_ip() #Get Ip's
    ip_tracker() #Get Ipinfo
    adjective()




if __name__ == "__main__":
    main_controller()
    track_record()
    pass