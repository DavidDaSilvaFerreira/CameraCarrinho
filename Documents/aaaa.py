import RPi.GPIO as GPIO
import time 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

porta =21
tempo = (0.016375671)

GPIO.setup(porta,GPIO.OUT)

def liga():
    GPIO.output(porta, GPIO.HIGH)
def desliga():
    GPIO.output(porta, GPIO.LOW)


liga()
