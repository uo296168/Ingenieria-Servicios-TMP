
import email.message
import email.policy
import email.utils

# Creamos el objeto que representa el mensaje
mensaje = email.message.EmailMessage()

# Configuramos las cabeceras
mensaje["To"] = "Destinatario <destinatario@example.com>"
mensaje["From"] = "Remitente <remitente@example.com>"
mensaje["Subject"] = "Mensaje de prueba"
mensaje["Date"] = email.utils.formatdate(localtime=True)
mensaje["Message-ID"] = email.utils.make_msgid()

# Introducimos el contenido del mensaje
mensaje.set_content("Esto es una prueba de envío de correo.")

# Convertimos el mensaje a bytes
binario = mensaje.as_bytes(policy=email.policy.SMTP)

# Mostramos el resultado
print(binario.decode("utf-8"))
