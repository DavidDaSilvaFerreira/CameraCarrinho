from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.capture('renatinha.jpg')
sleep(10)
