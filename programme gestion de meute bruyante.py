#--------------------programme de correction de meutes bruyantes-----------------
#le programme enregistre le son émi dans le chenil via un micro,
#le seuil de tolérance dépassé,il envoye un signal sonore
#et si dans un laps de temps T le seuil est a nouveau dépassé, un relais est alimenté
#qui va mettre en route une élétrovanne (dans le cas ou le chenil est équipé d'un groupe préssurisée
#ou une pompe dans le cas contraire.
# ATTENTION: capteur de son possiblement en analogique donc prévoir passage sur arduino
#-------------------------------------------------------------------------------

import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.Board)
GPIO.setwarnings(False)

#parametrage entrée micro-----------------------
micro= 36
GPIO.setmode (micro,GPIO.IN)
#paramètrage sortie relais buzzer---------------
buzzer= 38
GPIO.setmode (buzzer,GPIO.OUT)
#paramètrage sortie relais vanne-----------------
vanne= 40
GPIO.setmode (vanne,GPIO.OUT)

#---------------------coeur du programme----------
