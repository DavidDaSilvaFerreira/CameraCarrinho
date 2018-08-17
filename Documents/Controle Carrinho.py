import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
portaA = 4

GPIO.setup(4, GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
PWM = GPIO.PWM(4,61.066)
PWM2 = GPIO.PWM(17,61.066)
#time.sleep(2)

PWM.start(9.23)
#PWM2.start(10)

#PWM.ChangeDutyCycle(9.23)
#PWM2.ChangeDutyCycle(9.23)
time.sleep(2)
print 'Comecou'




arq = open('/home/pi/Documents/Arquivo1.txt', 'r') 
#texto = arq.readlines() 	
valores =[]
texto = arq.readlines()
for linha in texto :
    x = linha.split("\t")
    for i in x:
        valores.append(float (i))

for i in valores:
    PWM.ChangeDutyCycle(i)
    time.sleep(1/6)
arq.close()
print 'Finalizou'



#PWM2.ChangeDutyCycle(9.23)

PWM.stop()
PWM2.stop()
GPIO.cleanup()

