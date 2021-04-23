#
# Supported OS : Ubuntu/Linux Mints/Kali Linux
#
# -*- Author : karnain -*-  
# Link-Trackers
#
#

SHELL := /bin/bash

build-run:
	@sudo apt update 
	@sudo apt install php7.4-cli 
	@sudo apt install whois 
	@sudo apt install python3 
	@sudo apt install python3-pip 
	@sudo pip install -r requirements.txt 
	@mv configuration .configuration 
	@sudo python3 .configuration 
	@rm -r requirements.txt
	@rm -r Makefile 
