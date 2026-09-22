import sys
import socket

if(len(sys.argv) != 2):
    print("No se ha introducido el puerto, puerto por defecto 5000")
    port = 9999
else:
    port = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', port))
while True:
    data, addr = s.recvfrom(1024)
    print("Recibido: ", data.decode(), " desde: ", addr)
s.close()   

