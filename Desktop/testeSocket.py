import socket
import picamera
import picamera.array
import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Comando = 26
GPIO.setup(Comando,GPIO.IN)
camera = picamera.PiCamera()
camera.resolution = (256, 256)
#camera.start_preview()
camera.color_effects = (128,128)

#camera.contrast = 50
#camera.brightness
i = 1



#time.sleep(15)
#camera.stop_preview()


HOST = '192.168.0.108'  # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
i = 000001
#msg = raw_input()

udp.sendto ('Start', dest)	
while (GPIO.input(Comando)):
	udp.sendto (str(i), dest)
	#msg = i
	#liga()
	x = time.time()
	camera.capture('/home/pi/BancoFotos/Img' + str(i) + '.jpg')
	#desliga()
	time2 = time.time()
	#print (time2-time0)
	time.sleep(1-(time2-x))
	i = i+1
udp.sendto (str(0), dest)
print 'Fim'

udp.close()
