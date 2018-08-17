import picamera
import picamera.array




i = 2
while(i<4):
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            camera.resolution = (1920, 1080)
            #camera.capture(output, 'rgb')
            print("tirou")
            camera.capture("Ap/Photo" + str(i) +".jpg")
            i+=1
