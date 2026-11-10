import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.settimeout(2) #2 segundos de espera para recibir respuesta

if len(sys.argv) != 3:
    print("Usando el puerto 9999 por defecto e ip localhost")
    puerto = 9999
    ip = "localhost"
else:
    puerto = int(sys.argv[1])
    ip = sys.argv[2]

print("Introduce mensaje: ")
msg = input()
numero = 1
while msg != "FIN":
    s.sendto(f"{numero}: {msg}".encode(), (ip, puerto))

    try:
        datagrama, origen = s.recvfrom(1024) #1024 es el máximo tamaño esperado
        print("Respuesta del servidor:", datagrama.decode("utf-8"))

    except socket.timeout:
        print("No se ha recibido respuesta del servidor")

    msg = input()
    numero += 1

s.sendto(f"{numero}: {msg}".encode(), (ip, puerto))