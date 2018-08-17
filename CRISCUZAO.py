import time
import numpy as np
import picamera
import picamera.array
from PIL import Image
import pickle
#arq = open("/home/pi/BancoFotos/fotos1.csv",'w')
#writer = csv.writer(arq,delimiter = ',')
arq = open("/home/pi/BancoFotos/fotos1.txt","w", encoding = "utf-8")
#camera = picamera.PiCamera()
fotos = []
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        camera.resolution = (256, 256)
        a = time.time()
        camera.capture(output, 'rgb')
       
        #camera.capture('/home/pi/BancoFotos/foto.png')
        fotos = np.asarray(output.array).reshape(-1)
        print((time.time()-a))
        #arq.writelines(['%s,' %item for item in fotos])
        picle.dump(fotos, arq)
        #writer.write(fotos)
      
        print((time.time()-a))
        print("tirou")
        #ultimaFoto = camera.capture("Ap/Foto" + str(i) +".jpg")
        #Fotos.append(np.asarray(output.array).reshape(-1))

arq.write("teste")        
arq.close()
