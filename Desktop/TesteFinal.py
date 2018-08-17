import socket,pickle
from threading import Thread
from threading import Condition
import time
import numpy as np
import picamera 
import picamera.array
from PIL import Image
from picamera import PiCamera
import datetime
import os
import sys
finliza = 0
booleano = 'b'
ultimaFoto = []
date =datetime.datetime.now()
data = str(date.day) +"-"+str(date.month)+"-"+str(date.hour)+"-"+str(date.minute)
filePath = "/home/pi/BancoFotos/"+ data
print(filePath)
#diretorio = os.path.dirname(filePath)
os.mkdir(filePath)
class Cliente(Thread):
    def run(self):
        global booleano
        HOST = '192.168.1.109'
        PORT = 4000
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST,PORT)
        msgEnvio = "msg"
        i = 0
        camera = picamera.PiCamera()
        camera.start_preview()
        print("chegou")
        udp.sendto(data.encode('utf-8'),dest)
        while (booleano != 'x'):
            
            camera.resolution = (256, 256)
            #camera.start_preview() ##teste
            camera.capture(filePath+"/" +str(i)+'.png')
            
            #time.sleep(0.9)
            udp.sendto(str(i).encode('utf-8'), dest)
            i =i+1
            print("next image")
        print("Acabou fotos")
        udp.sendto("end".encode('utf-8'),dest)
        udp.close()
        sys.exit("finalmente cliente")

class Servidor(Thread):
    def run(self):
        global booleano
        HOST = ''
        PORT = 5000
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (HOST,PORT)
        udp.bind(orig)
        print("waiting")
        msg, cliente = udp.recvfrom(1024)
        print("e nois")
        booleano='x'
        udp.close()
        sys.exit("Finalmente Servidor")
        
        
        
#arq = open("/home/pi/BancoFotos/fotos1.txt","w")

Cliente().start()
Servidor().start()
booleano = input()
