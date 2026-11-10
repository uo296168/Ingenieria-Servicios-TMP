import sys
import socket

if len(sys.argv) != 2:
    print("No se ha indicado el puerto, se usará el 9999 por defecto")
    puerto = 9999
else:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", puerto))

s.listen(5)

while True:
    print("Esperando un cliente")

    sd, origen = s.accept()

    print("Nuevo cliente conectado desde %s, %d" % origen)

    continuar = True

    while continuar:
        datos = sd.recv(5)
        datos = datos.decode("ascii")

        if datos == "":
            print("Conexión cerrada de forma inesperada por el cliente")
            sd.close()
            continuar = False

        elif datos == "FINAL":
            print("Recibido mensaje de finalización")
            sd.close()
            continuar = False

        else:
            print("Recibido mensaje: %s" % datos)