#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
import RPi.GPIO as GP


GP.setmode(GP.BCM)
GP.setup(22,GP.OUT)

while True:
	GP.output (22,True)
	time.sleep(1)
	GP.output(22,False)
	time.sleep(1)

