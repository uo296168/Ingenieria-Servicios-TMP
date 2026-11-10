
import socket
import sys
import email.message
import email.policy
import email.utils
import ssl
import base64
import getpass


def RecvReply(s, codigo):
    while True:
        linea = b""

        # Recibimos una línea completa
        while not linea.endswith(b"\r\n"):
            byte = s.recv(1)

            if not byte:
                raise ConnectionError("Conexión cerrada por el servidor")

            linea += byte

        print(linea.decode("utf-8", errors="replace").strip())

        # Comprobamos el código SMTP
        if linea[:3] != codigo:
            print("Error: respuesta inesperada")
            sys.exit(1)

        # Un espacio indica la última línea de la respuesta
        if linea[3:4] == b" ":
            break


# Datos del servidor SMTP
server = "smtp.gmail.com"
port = 587

# Datos del correo electrónico
fromaddr = "uo296168@uniovi.es"
toaddr = "uo296168@uniovi.es"
subject = "Prueba SMTP desde Python"
data = "Este es mi primer correo enviado con sockets."


# Creamos el socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))

# Recibimos el saludo del servidor
RecvReply(s, b"220")

# Nos identificamos mediante EHLO
s.sendall(f"EHLO {socket.gethostname()}\r\n".encode("ascii"))
RecvReply(s, b"250")

# Solicitamos activar TLS
s.sendall(b"STARTTLS\r\n")
RecvReply(s, b"220")

# Creamos el contexto seguro
context = ssl.create_default_context()

# Convertimos el socket normal en uno cifrado
sc = context.wrap_socket(s, server_hostname=server)

print("Conexión TLS establecida correctamente")

# Volvemos a identificarnos a través del canal seguro
sc.sendall(f"EHLO {socket.gethostname()}\r\n".encode("ascii"))
RecvReply(sc, b"250")


# Solicitamos autenticarnos en Gmail
sc.sendall(b"AUTH LOGIN\r\n")
RecvReply(sc, b"334")

# Pedimos las credenciales por teclado
username = input("Usuario de Gmail: ")
password = getpass.getpass("Contraseña de aplicación: ")

# Enviamos el usuario codificado en Base64
sc.sendall(base64.b64encode(username.encode("ascii")) + b"\r\n")
RecvReply(sc, b"334")

# Enviamos la contraseña codificada en Base64
sc.sendall(base64.b64encode(password.encode("utf-8")) + b"\r\n")
RecvReply(sc, b"235")

print("Autenticación completada correctamente")


# Configuramos los datos del mensaje
fromaddr = username
toaddr = username  # Nos enviamos el correo a nosotros mismos
subject = "Prueba SMTP con Gmail"
data = "Este correo ha sido enviado desde Python utilizando TLS."

# Indicamos el remitente
sc.sendall(f"MAIL FROM:<{fromaddr}>\r\n".encode("ascii"))
RecvReply(sc, b"250")

# Indicamos el destinatario
sc.sendall(f"RCPT TO:<{toaddr}>\r\n".encode("ascii"))
RecvReply(sc, b"250")

# Solicitamos enviar el contenido
sc.sendall(b"DATA\r\n")
RecvReply(sc, b"354")

# Construimos el mensaje usando la biblioteca email
mensaje = email.message.EmailMessage(policy=email.policy.SMTP)

mensaje["To"] = toaddr
mensaje["From"] = fromaddr
mensaje["Subject"] = subject
mensaje["Date"] = email.utils.formatdate(localtime=True)
mensaje["Message-ID"] = email.utils.make_msgid()

mensaje.set_content(data)

# Convertimos el mensaje a bytes
binario = mensaje.as_bytes()

# Preparamos el mensaje para enviarlo mediante SMTP
if not binario.endswith(b"\r\n"):
    binario += b"\r\n"

# Escapamos los puntos al inicio de línea
binario = b"\r\n".join(
    b"." + linea if linea.startswith(b".") else linea
    for linea in binario.split(b"\r\n")
)

# Añadimos el terminador SMTP
binario += b".\r\n"

# Enviamos el mensaje
sc.sendall(binario)
RecvReply(sc, b"250")

print("Mensaje aceptado por el servidor SMTP")

# Cerramos la conexión SMTP
sc.sendall(b"QUIT\r\n")
RecvReply(sc, b"221")
sc.close()
