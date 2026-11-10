import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Usando el puerto 9999 por defecto e ip localhost")
    puerto = 9999
    ip = "localhost"
else:
    puerto = int(sys.argv[1])
    ip = sys.argv[2]

s.connect((ip, puerto)) # Conectarse al servidor

msg = input("Introduce mensaje (debe acabar en \\r\\n): ")
while msg != "" : 
    if msg[-4:] != "\\r\\n": # Los mensajes deben acabar con fin de línea o no estar vaciós, si no, se añade
        msg = msg + "\\r\\n"
    msg_real = msg.replace("\\r\\n", "\r\n") 
    s.sendall(msg_real.encode())
    respuesta = s.recv(80)
    respuesta_str = str(respuesta, "utf8")
    print(f"Respuesta recibida: {respuesta_str.strip()}")
    msg = input("Introduce mensaje (debe acabar en \\r\\n): ")

print("Cerrando la conexión...") # Cierra la conexión con el servidor
s.close()