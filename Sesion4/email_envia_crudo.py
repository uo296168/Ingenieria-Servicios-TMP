
import socket
import sys
import email.message
import email.policy
import email.utils

def RecvReply(s, codigo):
    # Recibimos hasta 1024 bytes del servidor
    respuesta = s.recv(1024)

    # Mostramos la respuesta recibida
    print(respuesta.decode("utf-8", errors="replace"))

    # Comprobamos el código de respuesta SMTP
    if respuesta[:3] != codigo:
        print("Error: respuesta inesperada del servidor")
        sys.exit(1)


# Datos del servidor SMTP
server = "relay.uniovi.es"
port = 25

# Datos del correo electrónico
fromaddr = "uo296168@uniovi.es"
toaddr = "uo296168@uniovi.es"
subject = "Prueba SMTP desde Python"
data = "Este es mi primer correo enviado con sockets."

# Creamos un socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecemos la conexión con el servidor SMTP
s.connect((server, port))

# Recibimos el mensaje de bienvenida del servidor
RecvReply(s, b"220")


# 1. Nos identificamos ante el servidor
s.sendall(f"HELO {socket.gethostname()}\r\n".encode("ascii"))
RecvReply(s, b"250")

# 2. Indicamos el remitente del correo
s.sendall(f"MAIL FROM:<{fromaddr}>\r\n".encode("ascii"))
RecvReply(s, b"250")

# 3. Indicamos el destinatario del correo
s.sendall(f"RCPT TO:<{toaddr}>\r\n".encode("ascii"))
RecvReply(s, b"250")

# Solicitamos enviar el contenido del correo
s.sendall(b"DATA\r\n")
RecvReply(s, b"354")


# Creamos el mensaje utilizando la biblioteca email
mensaje = email.message.EmailMessage(policy=email.policy.SMTP)

# Configuramos las cabeceras
mensaje["To"] = toaddr
mensaje["From"] = fromaddr
mensaje["Subject"] = subject
mensaje["Date"] = email.utils.formatdate(localtime=True)
mensaje["Message-ID"] = email.utils.make_msgid()

# Añadimos el contenido
mensaje.set_content(data)

# Convertimos el mensaje a bytes
binario = mensaje.as_bytes()

# Añadimos el terminador SMTP
if not binario.endswith(b"\r\n"):
    binario += b"\r\n"

binario += b".\r\n"

# Enviamos el mensaje
s.sendall(binario)
RecvReply(s, b"250")


# Enviamos el mensaje
s.sendall(message.encode("utf-8"))
RecvReply(s, b"250")


# Cerramos la conversación SMTP
s.sendall(b"QUIT\r\n")
RecvReply(s, b"221")
s.close()
