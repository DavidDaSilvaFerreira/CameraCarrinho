import picamera
import picamera.array
from PIL import Image
Fotos = []
arq=open('/home/pi/Documents/FotosArray.txt')

i=0

while i<2:
    i=i+1
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            camera.capture(output, 'rgb')
            Fotos.append(output.array)
            print('Captured %dx%d image' % (
                    output.array.shape[1], output.array.shape[0]))
            

x = Fotos.pop()

A = np.squeeze(np.asarray(x))

arq.writelines(A)
#im = Image.fromarray(x)

#im.save('Renata.jpg')



########
#text = []
#text.append()

arq.close()
