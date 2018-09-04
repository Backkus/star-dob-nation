#------------------
#affichage niveau puit
#et gestion niveau eau bassins
#Le but étant d'avoir,
#1>une requete de l'utilisateur qui donne le niveau du puit (entre 20% et 100%)
#2>un declenchement de la pompe qui est dans le puit en cas d'assechement des bassins pendant un laps de temps a définir
#3>[[[IMPORTANT]]] une mise en pause du programme qui demandera une input pour redemarrer si jamais la sonde 20% n'est plus immèrgée (pour proteger la pompe)
#toute les valeurs attribués sous formes de nombres sont des ports GPio 
#---------------------


import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.Board)
GPIO.setwarnings(False)

#---------paramètrage des 5 capteurs de niveau (20% >>>> 100%-------------

20%= 29
40%= 31
60%= 33
80%= 35
100%= 37

pin_niveau= [29.31.33.35.37]
GPIO.setmode (pin_niveau,GPIO.IN)

#-------------paramétrage sonde niveau bassins et relais pompe------------
bassin_amont= 11
bassin_aval= 13
bassins= [11.13]
GPIO.setmode (bassins,GPIO.IN)

relais_pompe= 12
GPIO.setmode (relais_pompe,GPIO.OUT)

#-------------coeur du programme------------------------------------------
  while true on verra ca un autre soir ma gamine pleure!