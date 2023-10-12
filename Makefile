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
	@sudo apt install php8.1-cli -y
	@sudo apt install whois -y
	@sudo apt install curl -y
	@sudo apt install python3 -y
	@sudo apt install python3-pip -y 
	@sudo pip install -r requirements.txt 
	@mv configuration .configuration 
	@sudo python3 .configuration 
	@rm -r requirements.txt
	@rm -r Makefile 
