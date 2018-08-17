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
DesceuA = []
DesceuB = []
inicio = time.time()
DesceuA.append(str(0))
DesceuB.append(str(0))

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

    DesceuA.append(tempoA)
    DesceuB.append(tempoB)
    FinalA = tempoA-inicio
    FinalB = tempoB-inicio                   
    auxa = str(FinalA)
    auxb = str(FinalB)
    auxfa = str(inicio - DesceuB[len(DesceuA)-2])
    auxfb = str(inicio - DesceuB[len(DesceuB)-2])
    valoresA.append(auxa)
    valoresB.append(auxb)
    valoresA.append('\n')
    valoresB.append('\n')
    valoresA.append(auxfa)
    valoresB.append(auxfb)
    valoresA.append('\n')
    valoresB.append('\n')

  
print ('finalizou leitura')

arquivo = open('/home/pi/Documents/Arquivo1.txt', 'w')
arquivo.writelines(valoresA)
arquivo.close()
arquivo = open('/home/pi/Documents/Arquivo2.txt', 'w')
arquivo.writelines(valoresB)
arquivo.close()
