#!/bin/bash

cd src
service openvswitch-switch start
mn -c
python init.py
screen -dmS main python run.py
tail -f /dev/null