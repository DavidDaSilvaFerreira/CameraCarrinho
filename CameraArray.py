import numpy as np
import picamera
import picamera.array
from PIL import Image


print ("Teste numpy")
lista = []
fotos = []
with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        camera.resolution = (256, 256)
        camera.capture
        camera.capture(output1, 'rgb')
        camera.color_effects = (128, 128)
        camera.capture(output, 'rgb')
        
        camera.capture("foto.png")
        fotos.append(output)
        print (output.array)
        lista.append(np.asarray(output.array).reshape(-1))
#print (lista[0])
print (len(lista[0]))




