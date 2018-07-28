from tkinter import *
import Temperature
import Moisture
class UI:



    def __init__(self):
        fenetre = Tk()
        fenetre.title("TEST INTERFACE CAPTEUR")

        temperature = Temperature.getGPIOTemperatureValue()
        cbTemperatureValue = IntVar()

        def clicked():
            if(cbTemperatureValue.get()):
                temperatureValue.configure(text=Temperature.temperatureKelvinFormat(temperature))
            else:
                temperatureValue.configure(text=Temperature.temperatureCelsiusFormat(temperature))

        # Temperature
        checkbuttonTemperature = Checkbutton(fenetre, text="Kelvin?", command=clicked, variable=cbTemperatureValue)
        checkbuttonTemperature.pack()


        temperatureLabel = Label(fenetre, text="Temperature:")
        temperatureLabel.pack()

        temperatureValue = Label(fenetre, text=Temperature.temperatureCelsiusFormat(temperature), bg="yellow")
        temperatureValue.pack()

        # Bouton de sortie
        boutonClose=Button(fenetre, text="Fermer", command=fenetre.quit)
        boutonClose.pack()

        fenetre.mainloop()



#def add_callback(pick_value, func, userdata = None):