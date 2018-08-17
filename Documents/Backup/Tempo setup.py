import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
portaA = 17
portaB = 4
controle = 22
GPIO.setup(22,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4, GPIO.OUT)


def Liga(RCpin):
    GPIO.setup(RCpin, GPIO.HIGH)

def Desliga(RCpin):
    GPIO.setup(RCpin, GPIO.LOW)



while 1:
    time0 = time.time()
    Liga(portaA)
    time1 = time.time()
    print (time1-time0)
    time2 = time.time()
    Desliga(portaA)
    time3 = time.time()
    print (time3-time2)
    
