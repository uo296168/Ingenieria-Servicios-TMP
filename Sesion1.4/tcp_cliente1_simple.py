import sys
import socket

if len(sys.argv) != 3:
    print("No se ha indicado la IP y el puerto, se usará localhost y 9999 por defecto")
    ip = "localhost"
    puerto = 9999
else:
    ip = sys.argv[1]
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, puerto))

for i in range(5):
    s.send(b"ABCDE")

s.send(b"FINAL")

s.close()