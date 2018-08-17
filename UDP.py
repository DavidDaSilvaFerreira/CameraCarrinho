import socket
from threading import Thread
import time
import numpy as np

vetor = []


class Cliente(Thread):
    def run(self):
        global vetor
        HOST = '192.168.0.108'  # Endereco IP do Servidor
        PORT = 5000            # Porta que o Servidor esta
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dest = (HOST, PORT)
        while True:
            if (len(vetor)>0):
                x = vetor.pop(0) + " a"
                udp.sendto (x, dest)
        udp.close()

class Servidor(Thread):
    def run(self):
        global vetor
        HOST = ''              # Endereco IP do Servidor
        PORT = 4000            # Porta que o Servidor esta
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        orig = (HOST, PORT)
        udp.bind(orig)
        msg = "seila"
        while msg != "end":
            msg, cliente = udp.recvfrom(1024)
            vetor.append(msg)
            print (msg)
        udp.close()
Cliente().start()
Servidor().start()
