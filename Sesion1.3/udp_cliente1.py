import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if len(sys.argv) != 3:
    print("Usando el puerto 9999 por defecto e ip localhost")
    puerto = 9999
    ip = "localhost"
else:
    puerto = int(sys.argv[1])
    ip = sys.argv[2]

print("Introduce mensaje: ")
msg = input()
while msg != "FIN":
    s.sendto(msg.encode(), (ip, puerto))
    msg = input()

s.sendto(msg.encode(), (ip, puerto))