
from telnetlib3 import Telnet
import getpass

HOST = "localhost"

usuario = input("Usuario: ")
clave = getpass.getpass("Contraseña: ")

tn = Telnet(HOST, 23)

# Autenticación
tn.read_until(b"login: ")
tn.write(usuario.encode("utf-8") + b"\n")

tn.read_until(b"Password: ")
tn.write(clave.encode("utf-8") + b"\n")

# Descartar el mensaje de bienvenida
bienvenida = tn.read_until(b"$", timeout=10)

if b"$" not in bienvenida:
    print("Error al iniciar sesión:")
    print(bienvenida.decode("utf-8", errors="replace"))
    tn.close()
    exit(1)

# Ejecutar el comando remoto
tn.write(b"ls /home\n")

# Recibir únicamente la respuesta del comando
respuesta = tn.read_until(b"$", timeout=10)

print(respuesta.decode("utf-8", errors="replace"))

# Cerrar la sesión
tn.write(b"exit\n")
tn.close()
