#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
#GPIO SETUP
channelMoisture = 21
channelLed = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(channelMoisture, GPIO.IN)
GPIO.setup(channelLed,GPIO.OUT)
GPIO.setwarnings(False)
"""while True:
	GP.output (channelLed,True)
	time.sleep(1)
	GP.output(channelLed,False)
	time.sleep(1)"""


 
print (GPIO.input(channelMoisture))
if GPIO.input(channelMoisture) == 0:
    print ("ya de l'eau enculé")
    GPIO.output (channelLed,True)
else:
    print ("ya pas d'eau enculé")
    GPIO.output (channelLed,False)
