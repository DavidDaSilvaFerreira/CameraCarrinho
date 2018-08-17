import picamera
import picamera.array
import time

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.start_recording('Ap/Video.h264')
    print("Comecou gravar")
    time.sleep(60)
    camera.stop_recording()
    camera.stop_preview()
    print("Terminou Gravar")
