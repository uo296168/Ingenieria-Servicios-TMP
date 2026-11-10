
from telnetlib3 import Telnet
import getpass

HOST = "localhost"

usuario = input("Usuario: ")
clave = getpass.getpass("Contraseña: ")

# Conectar al servidor Telnet
tn = Telnet(HOST, 23)

# Autenticación
tn.read_until(b"login: ") #esperamos hasta que el servidor devuelva login
tn.write(usuario.encode("utf-8") + b"\n") #enviamos la respuesta al servidor

tn.read_until(b"Password: ") 
tn.write(clave.encode("utf-8") + b"\n")

# Esperar a que el shell esté preparado
respuesta = tn.read_until(b"$", timeout=10)

if b"$" not in respuesta: #si el servidor no esta preparado para recibir comandos...
    print("No se ha detectado el prompt del shell.")
    print(respuesta.decode("utf-8", errors="replace"))
    tn.close()
    exit(1)

# Ejecutar comando remoto
tn.write(b"ls /home\n")

# Cerrar sesión
tn.write(b"exit\n")

# Recibir y mostrar la respuesta
respuesta = tn.read_all()
print(respuesta.decode("utf-8", errors="replace"))

tn.close()

