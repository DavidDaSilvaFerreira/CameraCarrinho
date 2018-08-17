from io import BytesIO
from time import sleep
import picamera
from PIL import Image
import numpy as np


stream = BytesIO()
camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.start_recording(stream, format='h264', quality=23)
camera.wait_recording(15)
camera.stop_recording()
