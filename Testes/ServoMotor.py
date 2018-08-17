import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
portaA = 17
portaB = 4
controle = 22
GPIO.setup(22,GPIO.IN)
GPIO.setup(17,GPIO.IN)
GPIO.setup(4, GPIO.IN)
valoresA = []
valoresB = []
inicio = time.time()
frequencia = float(100/61.066)
while(GPIO.input(controle)):
    i=0
    tempo=0
    while(not(GPIO.input(portaA))):
        if(not(GPIO.input(controle))):
            break   
    inicio = time.time()
    while((GPIO.input(portaA)) and (GPIO.input(portaB))):
        if(not(GPIO.input(controle))):
            break 
    if(not(GPIO.input(portaA))):
        tempoA = time.time()
        while (GPIO.input(portaB)):
                h=0
        tempoB= time.time()
    else:
        tempoB = time.time()
        while (GPIO.input(portaA)):
                h=0
        tempoA= time.time()
        
    
    FinalA = (tempoA-inicio)/(frequencia)
    FinalB = (tempoB-inicio)/(frequencia)
    auxa = str(FinalA)
    auxb = str(FinalB)
    valoresA.append(auxa)
    valoresB.append(auxb)
    #valores.append(str(aux))
    valoresA.append('\n')
    valoresB.append('\n')


  
print ('finalizou leitura')

arquivo = open('/home/pi/Documents/Arquivo1.txt', 'w')
arquivo.writelines(valoresA)
arquivo.close()
arquivo = open('/home/pi/Documents/Arquivo2.txt', 'w')
arquivo.writelines(valoresB)
arquivo.close()                   

