#!/usr/bin/python3
# -*- Author : karnain -*-    
#
# This user interface provides users with a command console interface to the
# Framework.
#

import os as console
from configparser import ConfigParser
import subprocess as system

add = {}

class main:
    def initialize(require):
        global add
        if console.path.isfile(require):
            add = ConfigParser()
            add.read(require)
            add["include"] = { 
                'banner': add.get('require','banner'),
                'system': add.get('require','system')
            }
            return True

    def HacktivityAction():
        PATH = add["include"]["banner"]
        console.system("clear")
        system.run(["python3", PATH])

    initialize(console.path.join(console.path.dirname(console.path.realpath(__file__))) + "/config/LinkTracker.cfg")
    HacktivityAction()

def main_control():
    try:
        PATH = add["include"]["system"]
        system.run(["python3", PATH])
    except EOFError:
        console.system("clear")
    pass


if __name__ == "__main__":
    main()
    main_control()
