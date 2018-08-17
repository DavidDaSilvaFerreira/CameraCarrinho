from PIL import Image
import numpy as np
import picamera
import picamera.array
import socket,pickle
from threading import Thread
from threading import Condition
import time

#img is a np array with shape (3,256,256)

print ("oi")

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        camera.resolution = (256, 256)
        camera.capture(output, 'rgb')
        print("tirou")
        img = []
        img=(np.asarray(output.array).reshape(-1))
        print(str(img))
        u = Image.fromarray(np.array(img))
        u.show()
