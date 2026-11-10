import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if len(sys.argv) != 3:
    print("Usando el puerto 9999 por defecto e ip localhost")
    puerto = 9999
    ip = "localhost"
else:
    puerto = int(sys.argv[1])
    ip = sys.argv[2]

print("Introduce mensaje: ")
msg = input()
numero = 1

while msg != "FIN":

    timeout = 0.5

    while timeout <= 2:
        s.settimeout(timeout)

        s.sendto(f"{numero}: {msg}".encode(), (ip, puerto))

        try:
            datagrama, origen = s.recvfrom(1024)

            if datagrama.decode("utf-8") == "OK":
                break

        except socket.timeout:
            print("No se ha recibido respuesta del servidor, reintentando...")
            timeout *= 2

    if timeout > 2:
        print("Puede que el servidor esté caído. Inténtelo más tarde")
        sys.exit(1)

    msg = input()
    numero += 1