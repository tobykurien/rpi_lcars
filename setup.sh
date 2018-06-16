#!/bin/sh
sudo apt-get update
sudo apt-get install python3 python3-pip libopenjp2-7-dev

sudo pip3 install -r requirements.txt

# on dietpi/raspbian lite install xinit
sudo apt-get install xinit
