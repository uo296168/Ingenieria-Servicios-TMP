import socket
import sys
import random

if len(sys.argv) != 2:
    print("Usando el puerto 9999 por defecto")
    puerto = 9999
else:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", puerto))

while True:
    datagrama, origen = s.recvfrom(1024) #1024 es el máximo tamaño esperado
    numeroaleatorio = random.randint(1, 10)
    if(numeroaleatorio % 2 == 0):
        print("Se ha perdido el datagrama")
    else:
        print("Se ha recibido un datagrama desde desde", origen)
        print("Contiene lo siguiente: ")
        print(datagrama.decode("utf-8"))
        s.sendto(datagrama, origen)
