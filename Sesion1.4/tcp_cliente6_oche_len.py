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

msg = input("Introduce mensaje: ")
while msg != "" : 
    mensaje = msg.encode("utf8")
    s.sendall(str(len(mensaje)).encode("ascii") + b"\n" + mensaje)
    
    longitud = b""
    while not longitud.endswith(b"\n"):
        dato = s.recv(1)
        if dato == b"":
            break
        longitud += dato
    if not longitud.endswith(b"\n"):
        print("El servidor ha cerrado la conexión")
        break
    
    faltan = int(longitud[:-1])
    respuesta = b""
    while len(respuesta) < faltan:
        dato = s.recv(faltan - len(respuesta))
        if dato == b"":
            break
        respuesta += dato
    if len(respuesta) != faltan:
        print("El servidor ha cerrado la conexión durante la respuesta")
        break

    respuesta_str = str(respuesta, "utf8")
    print(f"Respuesta recibida: {respuesta_str}")
    msg = input("Introduce mensaje: ")

print("Cerrando la conexión...") # Cierra la conexión con el servidor
s.close()