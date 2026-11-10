import socket
import sys

puerto = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
msg = "BUSCANDO HOLA"
ip = sys.argv[1]
s.sendto(msg.encode("utf-8"), (ip, puerto))

s.settimeout(2) #2 segundos de espera para recibir respuesta

servidor = None

while True:
    try:
        datagrama, origen = s.recvfrom(1024)
        print("Respuesta del servidor:", datagrama.decode("utf-8"), "desde", origen)
        if servidor is None:
            servidor = origen
    except socket.timeout:
        print("No se ha recibido respuesta del servidor")
        break

if servidor is not None:
    s.sendto("HOLA".encode("utf-8"), servidor)
    datagrama, origen = s.recvfrom(1024)
    print("Respuesta del servidor: ", datagrama.decode("utf-8"))
    
    