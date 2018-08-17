


from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
camera = PiCamera
captura = PiRGBArray(camera)
camera.capture(captura, format = 'bgr')
imagem = captura.array

cv2.imshow("Image",imagem)
