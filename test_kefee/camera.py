
#from time import clock
from time import time
from time import sleep
from picamera import PiCamera



camera = PiCamera()
camera.resolution = (1280, 720)
camera.start_preview()


sleep(5)
timeString = str(time())

camera.capture('testPhoto('+timeString+').jpg')
camera.stop_preview()