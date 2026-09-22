import sys
import socket
import random

if(len(sys.argv) != 2):
    print("No se ha introducido el puerto, puerto por defecto 5000")
    port = 9999
else:
    port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', port))

while True:
    rnd = random.randint(0, 1)
    data, addr = s.recvfrom(1024)
    if rnd >= 0.5:
        data, addr = s.recvfrom(1024)
        print("Recibido: ", data.decode(), " desde: ", addr)
    else: 
        print("Simulando perdida de paquete")
s.close()   