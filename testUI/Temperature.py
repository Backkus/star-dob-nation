

def getGPIOTemperatureValue():
    return 25

def temperatureCelsiusFormat(temperature):
    result = str(temperature)+"°"
    return result

def temperatureKelvinFormat(temperature):
    result = str(temperature+273.15)+"k"
    return result