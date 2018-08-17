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

#output = picamera.array.PiRGBArray(camera)
#
def Cliente():

    i =0
    arq = open('/home/pi/thetcheka.txt','w')    
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            while (i<5):
                camera.resolution = (256, 256)
                y = time.time()
                camera.capture(output, 'rgb')
                Fotos.append(np.asarray(output.array).reshape(-1))
                #for q in Fotos[0]:
                 #   print(q)
                x = time.time()
                print(x-y)
                #text = ' '.join(str(e) for e in Fotos.pop(0))
                
                #arq.write(text)
                #condicao.notify()
                #print("Tirou foto")
                i = i +1
    print("Acabou fotos")
    arq.close()

Cliente()
