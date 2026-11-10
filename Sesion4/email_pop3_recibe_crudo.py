
import socket
import ssl
import sys
import getpass

from email import policy
from email.parser import BytesParser


def RecvReply(s):
    respuesta = b""

    # Leemos hasta encontrar el final de línea
    while not respuesta.endswith(b"\r\n"):
        byte = s.recv(1)

        if not byte:
            raise ConnectionError("El servidor ha cerrado la conexión")

        respuesta += byte

        if len(respuesta) > 1024:
            raise ValueError("Respuesta POP3 demasiado larga")

    print(respuesta.decode("utf-8", errors="replace").strip())

    # Comprobamos que la respuesta sea correcta
    if respuesta[:3] != b"+OK":
        print("Error: respuesta inesperada del servidor")
        sys.exit(1)

    return respuesta


# Configuración del servidor POP3
server = "pop.gmail.com"
port = 995

# Creamos la conexión TCP
s = socket.socket()
s.connect((server, port))

# Establecemos la conexión cifrada
context = ssl.create_default_context()
sc = context.wrap_socket(s, server_hostname=server)

# Recibimos el saludo del servidor
RecvReply(sc)


# Solicitamos las credenciales
username = input("Usuario de Gmail: ")
password = getpass.getpass("Contraseña de aplicación: ")

# Enviamos el usuario
sc.sendall(f"USER {username}\r\n".encode("utf-8"))
RecvReply(sc)

# Enviamos la contraseña
sc.sendall(f"PASS {password}\r\n".encode("utf-8"))
RecvReply(sc)


# Consultamos cuántos mensajes tenemos
sc.sendall(b"STAT\r\n")
respuesta = RecvReply(sc)

# Extraemos el número de mensajes
num_mensajes = int(respuesta.split()[1])

print("Mensajes disponibles:", num_mensajes)

if num_mensajes > 0:

    # Solicitamos el primer correo
    sc.sendall(b"RETR 1\r\n")
    RecvReply(sc)

    # Recibimos el mensaje completo
    contenido = b""

    while b"\r\n.\r\n" not in contenido:
        bloque = sc.recv(4096)

        if not bloque:
            raise ConnectionError("Conexión cerrada durante RETR")

        contenido += bloque

    # Eliminamos el terminador POP3
    contenido = contenido.split(b"\r\n.\r\n", 1)[0] + b"\r\n"

    # Restauramos los puntos escapados por POP3
    if contenido.startswith(b".."):
        contenido = contenido[1:]

    contenido = contenido.replace(b"\r\n..", b"\r\n.")

    # Interpretamos el mensaje recibido
    mensaje = BytesParser(policy=policy.default).parsebytes(contenido)

    # Extraemos las cabeceras solicitadas
    print("From:", mensaje.get("From", "<desconocido>"))
    print("Subject:", mensaje.get("Subject", "<sin asunto>"))

else:
    print("No hay correos disponibles para descargar.")


# Cerramos la sesión
sc.sendall(b"QUIT\r\n")
RecvReply(sc)
sc.close()

