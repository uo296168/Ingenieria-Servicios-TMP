import socket
import sys

puerto = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(("", puerto))

while True:
    datagrama, origen = s.recvfrom(1024)
    if datagrama == "BUSCANDO HOLA".encode("utf-8"):
        s.sendto("IMPLEMENTO HOLA".encode("utf-8"), origen)
    elif datagrama == "HOLA".encode("utf-8"):
        s.sendto("HOLA".encode("utf-8") + origen[0].encode("utf-8"), origen)