
from telnetlib3 import Telnet
import time

HOST = "localhost"
USUARIO = "uo296168"
CLAVE = "Holabuenas913"

# Conectar mediante Telnet
tn = Telnet(HOST, 23)

# Autenticación
tn.read_until(b"login: ")
tn.write(USUARIO.encode("utf-8") + b"\n")

tn.read_until(b"Password: ")
tn.write(CLAVE.encode("utf-8") + b"\n")

# Esperar a que el shell esté preparado
tn.read_until(b"$")

# Consultar los procesos activos
tn.write(b"ps -efww\n")

# Recoger la respuesta
respuesta = tn.read_until(b"$")

# Comprobar si el servidor UDP está ejecutándose
if b"udp_servidor3_con_ok.py" in respuesta:
    print("El servidor ya está en ejecución")

else:
    print("El servidor no está en ejecución. Arrancándolo...")

    # Arrancar el servidor en segundo plano
    tn.write(b"nohup python3 udp_servidor3_con_ok.py &\n") 

    # Esperar un segundo para que arranque
    time.sleep(1)

# Cerrar la sesión remota
tn.write(b"exit\n")

# Mostrar la respuesta para depuración
salida = tn.read_all()
print(salida.decode("utf-8", errors="replace"))

tn.close()

