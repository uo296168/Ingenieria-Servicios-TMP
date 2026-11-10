
import smtplib
import ssl
import getpass
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from email.policy import SMTP

# Configuración del servidor
server = "smtp.gmail.com"
port = 587

# Credenciales
username = input("Usuario de Gmail: ")
password = getpass.getpass("Contraseña de aplicación: ")

# Datos del mensaje
fromaddr = username
toaddr = username
subject = "Prueba de envío con smtplib"
data = "Este correo ha sido enviado desde Python usando smtplib."

# Creamos el mensaje
mensaje = EmailMessage(policy=SMTP)

mensaje["To"] = toaddr
mensaje["From"] = fromaddr
mensaje["Subject"] = subject
mensaje["Date"] = formatdate(localtime=True)
mensaje["Message-ID"] = make_msgid()

mensaje.set_content(data)

# Conectamos con el servidor SMTP
with smtplib.SMTP(server, port, timeout=15) as s:

    # Activamos la depuración
    s.set_debuglevel(1)

    # Establecemos un canal seguro
    s.starttls(context=ssl.create_default_context())

    # Ocultamos las credenciales del registro de depuración
    s.set_debuglevel(0)

    # Nos autenticamos en Gmail
    s.login(username, password)

    # Reactivamos la depuración
    s.set_debuglevel(1)

    # Enviamos el mensaje
    s.sendmail(fromaddr, toaddr, mensaje.as_bytes())

print("Mensaje aceptado por el servidor SMTP")
