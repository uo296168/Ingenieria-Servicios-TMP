import sys
import socket

if(len(sys.argv) != 3):
    print("No se ha introducido la IP y el puerto, IP por defecto localhost y puerto por defecto 5000")
    ip = 'localhost'
    port = 9999
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n = 0
msg = input("Introduce el mensaje a enviar: ")

while(msg != "FIN"):
    n += 1
    s.sendto(f"{n}: {msg}".encode(), (ip, port))
    msg = input("Introduce el mensaje a enviar: ")  