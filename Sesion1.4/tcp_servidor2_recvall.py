import sys
import socket


def recvall(sock, n): #Función para recibir n bytes de datos del socket
    datos = b"" #Bytes vacíos

    while len(datos) < n:
        parte = sock.recv(n - len(datos)) #Restamos los bytes que ya hemos recibido para recibir solo los que faltan

        if parte == b"": #Si no se reciben datos, significa que la conexión se ha cerrado de forma inesperada
            return datos

        datos += parte #Si se reciben datos, los añadimos a los datos recibidos

    return datos


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

        datos = recvall(sd, 5)
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