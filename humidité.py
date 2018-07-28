#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
print (GPIO.input(channel))
if GPIO.input(channel) == 0:
	print ("ya de l'eau enculé")
else:
	print ("ya pas d'eau enculé")		
