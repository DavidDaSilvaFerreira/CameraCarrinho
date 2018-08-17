import picamera
import picamera.array
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Pulso = 26
GPIO.setup(Pulso,GPIO.OUT)
camera = picamera.PiCamera()
camera.resolution = (256, 256)
#camera.start_preview()
camera.color_effects = (128,128)

#camera.contrast = 50
#camera.brightness
i = 0

#time.sleep(15)
#camera.stop_preview()

def liga():
    GPIO.output(Pulso, GPIO.HIGH)
def desliga():
    GPIO.output(Pulso, GPIO.LOW)

#time.sleep(0.016)
while True:
        #time0 = time.time()
        #camera.image_effect = hatch
        liga()        
        camera.capture('/home/pi/BancoFotos/Img' + str(i) + '.jpg')
        desliga()
        #time2 = time.time()
        #print (time2-time0)
        i = i + 1
        
exit()
