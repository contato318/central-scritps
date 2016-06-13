#!/bin/bash
source env/bin/activate
killall central_scripts.py
nohup ./central_scripts.py  >> central.log &
ls -ltra

