import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
portaA = 17
portaB = 4
GPIO.setup(portaA,GPIO.OUT)
GPIO.setup(portaB, GPIO.OUT)


def Liga(RCpin):
    GPIO.setup(RCpin, GPIO.HIGH)

def Desliga(RCpin):
    GPIO.setup(RCpin, GPIO.LOW)


while 1:
    Liga(portaA)
    Desliga(portaB)


