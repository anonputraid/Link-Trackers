# -*- Author : Ytn4en -*-   

import time
from random import choice
import os as console
from configparser import ConfigParser
from colorama import Fore, Back, Style
###
#
# Module that contains some most excellent banners.
#
###

import glob as Include

add = {}

class main:
    def banner(expand_path):
        add = ConfigParser()
        add.read(expand_path)
        add["include"] = {
            'root': add.get('require','root'), 
        }
        absolute_path = Include.glob("{}/data/logos/*.txt".format(add["include"]["root"]))
        for x in range(1):
            Logos_banner = choice(absolute_path)
            if console.path.isfile(Logos_banner):
                Logos = open(Logos_banner)
                print(Fore.CYAN + Logos.read() + Style.RESET_ALL)
                pass
                

if __name__ == "__main__":
    main.banner(console.path.join(console.path.dirname(console.path.realpath(__file__))) + "/.config.cfg")
    pass