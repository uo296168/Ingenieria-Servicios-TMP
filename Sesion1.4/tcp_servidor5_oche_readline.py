import socket
import sys
import time

if len(sys.argv) != 2:
    print("Usando el puerto 9999 por defecto")
    puerto = 9999
else:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", puerto))
s.listen()

while True:
    sd, dir = s.accept()
    time.sleep(1)

    # Convertimos el socket en un fichero para usar readline()
    f = sd.makefile(encoding="utf8", newline="\r\n")

    while True:
        mensaje = f.readline()
        if not mensaje:
            break

        # readline() devuelve la cadena decodificada con el \r\n incluido al final
        linea = mensaje[:-2] 
        linea = linea[::-1]

        print("Se ha recibido un datagrama desde", dir)
        print("Contiene lo siguiente: ")
        print(f"{linea}")

        # Seguimos usando el socket directamente para escribir
        sd.sendall(bytes(linea + "\r\n", "utf8"))
        
    print(f"El cliente {dir} ha cerrado la conexión.")
    f.close() # Es buena práctica cerrar el objeto fichero
    sd.close()