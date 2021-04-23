#!/usr/bin/python3 
# -*- Author : Karnain

import sys
import os as console
from configparser import ConfigParser
import subprocess as system
import time as pomodoro
from colorama import Fore, Back, Style


add = {}

class compatibility:
    def initialize(require):
        global add
        if console.path.isfile(require):
            add = ConfigParser()
            add.read(require)
            add["include"] = { 
                'bin' : add.get('require','path'),
                'root': add.get('require','root'),
                'php' : add.get('require','php')
            }
            return True

    def dependencies():
        class Equipment:
            def download():
                console.chdir(add["include"]["php"])
                PIPE = 'https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip'
                console.system("wget {} > /dev/null 2>&1".format(PIPE))
                if console.path.isfile("ngrok-stable-linux-386.zip"):
                    console.system("unzip ngrok-stable-linux-386.zip > /dev/null 2>&1")
                    console.system("chmod +x ngrok")
                    console.remove("ngrok-stable-linux-386.zip")
                    pass
                else:
                    print(Fore.RED + "\n[-] Download Error... "+ Style.RESET_ALL )
                pass

        Path = add["include"]["php"]
        if console.path.isfile(Path + "/ngrok"):
            console.chdir(add["include"]["bin"])
            system.run(["python3","action_controller.py"]) # Start HTTP Server
            system.run(["python3","action_quickstart.py"]) # Start Tracking 
            system.run(["python3","action_information.py"])
        else:
            print(Fore.GREEN + "[+] Downloads Tunnels To Localhost"+ Style.RESET_ALL)
            Equipment.download()

    Intr = input(Fore.GREEN + "[*] Starting HTTP Server ?? Y/N : " + Fore.WHITE).lower()
    if Intr == "y":
        initialize(console.path.join(console.path.dirname(console.path.realpath(__file__))) + "/.config.cfg")
        dependencies()
    pass

if __name__ == "__main__":
    compatibility()
    pass