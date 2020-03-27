#!/bin/bash

service openvswitch-switch start
mn -c
screen -dmS main python run.py
tail -f /dev/null