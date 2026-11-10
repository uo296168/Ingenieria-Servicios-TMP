import socket
import sys
import time

if len(sys.argv) != 2:
    print("Usando el puerto 9999 por defecto")
    puerto = 9999
else:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crear socket TCP
s.bind(("", puerto))
s.listen() # Socket modo pasivo, a la espera de conexiones entrantes

while True:
    sd, dir = s.accept() # Recibir la conexión de un cliente
    # Primero recibir el mensaje del cliente
    
    time.sleep(1)

    while True:
        longitud = b""
        while not longitud.endswith(b"\n"):
            dato = sd.recv(1)
            if dato == b"":
                break
            longitud += dato
        if not longitud.endswith(b"\n"):
            break # El cliente ha cerrado la conexión.
        
        faltan = int(longitud[:-1])
        mensaje = b""
        while len(mensaje) < faltan:
            dato = sd.recv(faltan - len(mensaje))
            if dato == b"":
                break
            mensaje += dato
        if len(mensaje) != faltan:
            break

        linea = str(mensaje, "utf8")
        linea = linea[::-1]

        #imprimir la respuesta en pantalla
        print(f"{dir}: {linea}")

        respuesta = linea.encode("utf8")
        sd.sendall(str(len(respuesta)).encode("ascii") + b"\n" + respuesta)
        
    print(f"El cliente {dir} ha cerrado la conexión.")
    sd.close()  # Cerrar el socket del cliente