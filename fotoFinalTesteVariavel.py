import socket,pickle
from threading import Thread
from threading import Condition
import time
import numpy as np
import picamera
import picamera.array
from PIL import Image

Fotos = []
vetor = []
finliza = 0
booleano = 0
ultimaFoto = []
class Cliente(Thread):
    def run(self):
        global booleano
        #HOST = '192.168.0.108'
        #PORT = 4000
        #udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #dest = (HOST,PORT)
        msgEnvio = "msg"
        i = 0
        while (True):
            with picamera.PiCamera() as camera:
                with picamera.array.PiRGBArray(camera) as output:
                    print(output)
                    camera.resolution = (256, 256)
                    camera.capture(output, 'rgb')
                    print("tirou")
                    #ultimaFoto = camera.capture("Ap/Foto" + str(i) +".jpg")
                    Fotos.append(np.asarray(output.array).reshape(-1))
                    print(len(Fotos[-1]))
                    vetor.append( str(Fotos[-1]) + "testePWM")
                    grava()
                    #condicao.notify()
                    #print("Tirou foto")
          #  udp.sendto(msgEnvio, dest)
        print("Acabou fotos")
        #udp.sendto("end",dest)
        #udp.close()
        
class Servidor(Thread):
    def run(self):
        global vetor
        global booleano
        HOST = ''              # Endereco IP do Servidor
        PORT = 5000            # Porta que o Servidor esta
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (HOST, PORT)
        udp.bind(orig)
        msg = "seila"
        while msg != "end":
            msg, cliente = udp.recvfrom(1024)
            Fotos[-1].append(msg)
        print("gravando")
        booleano =1
        
        udp.close()


class Cliente2PC(Thread):
    def run(self):
        HOST2 = '192.168.0.109'
        PORT2 = 5050
        udp2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest2 = (HOST2,PORT2)
        i =0
        while (booleano != 1):
            cont = 0
            while(cont<5):
                condicao.acquire()
                cont = cont + 1
                dados = Fotos.pop(0)
                fotosMsg = ' '.join(str(e) for e in dados)
                
                
                #texto = ' '.join(str(e) for e in Dados)
                #texto = texto + vetor.pop(0)
                texto = "UDP> TCP"
                
                udp2.sendto(fotosMsg, dest2)
        print("Acabou fotos")
        udp2.sendto("end",dest2)
        udp2.close()



class ClientePC(Thread):
    def run(self):
        global vetor
        HOST = '192.168.0.109'
        PORT = 5050
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        cont = 0
        while(cont<5):
            if len(Fotos)==0:
                condicao.wait()
            condicao.acquire()
            cont = cont + 1
            Dados = Fotos.pop(0)
            print(len(Dados))
            condicao.release()
            #texto = ' '.join(str(e) for e in Dados)
            #texto = texto + vetor.pop(0)
            texto = "UDP> TCP"
            s.send(texto)
        s.close()

def grava():
    #Cliente().stop()
    #Servidor().stop()
    #arq = open("/home/pi/BancoFotos/fotos1.txt","w")
    print("abriu arquivo")
    #print(len(Fotos))
    #np.concatenate((Fotos, vetor.T), axis=1)
    cont = 0
    for i in Fotos:
        for e in i:
            arq.write(str(e))
            arq.write(",")
        arq.write(" saida ")
        arq.write(vetor[cont])
        arq.write("!")
        cont+=1
        arq.write("\n")
        print("foi uma")
    
    print("gravou")
    arq.close
    exit()
def grava1():
    #Cliente().stop()
    #Servidor().stop()
    print("abriu arquivo")
    #np.concatenate((Fotos, vetor.T), axis=1)
    cont = 0
    for i in Fotos:
        text = ""
        for e in i:
            
            text.append((e))
            text.append(" ")
        text.append((vetor[cont]))
        text.append("\n")
        cont+=1
        arq.write(text)
        print("foi uma")
    print("gravou")
    arq.close
    
arq = open("/home/pi/BancoFotos/fotos1.txt","w")

Cliente().start()
#Servidor().start()


#Cliente().exit()
#Servidor().exit()
while(booleano == 0):
      h=0
      
grava()
#Cliente2PC().start()
    
