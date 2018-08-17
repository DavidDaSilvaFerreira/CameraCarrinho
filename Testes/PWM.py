import RPi.GPIO as GPIO
import time
import wiringPI



GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
PortaPWM = GPIO.PWM(12,61)
PortaPWM.start(9.375)
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
tempoBaixoA = 0
tempoBaixoB = 0
inicio = time.time()
while(GPIO.input(controle)):
    i=0
    tempo=0
    while(not(GPIO.input(portaA))):
        if(not(GPIO.input(controle))):
            break   
    inicio = time.time()
    tempoAuxA = inicio - tempoBaixoA
    tempoAuxB = inicio - tempoBaixoB
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
        

    FinalA = tempoA-inicio
    FinalB = tempoB-inicio
    tempoBaixoA = FinalA
    tempoBaixoB = FinalB
    DC = ((FinalA/(1/61.066))*100)
    print (DC)
    PortaPWM.ChangeDutyCycle(DC)
    auxa = str(FinalA)
    auxb = str(FinalB)
    auxfa = str(tempoAuxA)
    auxfb = str(tempoAuxB)
    valoresA.append(auxa)
    valoresB.append(auxb)
    #valores.append(str(aux))
    valoresA.append('\n')
    valoresB.append('\n')
    valoresA.append(auxfa)
    valoresB.append(auxfb)
    valoresA.append('\n')
    valoresB.append('\n')

  
print ('finalizou leitura')
GPIO.cleanup()
arquivo = open('/home/pi/Documents/Arquivo1.txt', 'w')
arquivo.writelines(valoresA)
arquivo.close()
arquivo = open('/home/pi/Documents/Arquivo2.txt', 'w')
arquivo.writelines(valoresB)
arquivo.close()                   

