import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
porta = 17
comando = 22
GPIO.setup(22,GPIO.IN)
GPIO.setup(17,GPIO.IN)
valores = []

while(GPIO.input(22)):
    i=0
    tempo=0
    while(not(GPIO.input(17))):
        if(not(GPIO.input(22))):
            break   
    inicio = time.time()
    while(GPIO.input(17)):
        if(not(GPIO.input(22))):
            break       
    fim = time.time()
    tempo= fim-inicio 
    #print(tempo)
    #aux = int(tempo)/60
    aux = str(tempo)
    valores.append(aux)
    #valores.append(str(aux))
    valores.append('\n')

  
print ('finalizou leitura')

arquivo = open('/home/pi/Documents/Arquivo1.txt', 'w')
arquivo.writelines(valores)
arquivo.close()


