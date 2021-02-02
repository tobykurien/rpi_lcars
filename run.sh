#!/bin/sh
cd app

if [-z $DISPLAY]; then
  xinit /usr/bin/python3 lcars.py
else
  /usr/bin/python3 lcars.py
fi
