import socket
import sys
import time

if len(sys.argv) != 2:
    print("Usando el puerto 9999 por defecto")
    puerto = 9999
else:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Crear socket TCP
s.bind(("", puerto))
s.listen() # Socket modo pasivo, a la espera de conexiones entrantes

while True:
    sd, dir = s.accept() # Recibir la conexión de un cliente
    # Primero recibir el mensaje del cliente
    
    time.sleep(1)

    while True:
        mensaje = sd.recv(80)  # Nunca enviará más de 80 bytes, aunque tal vez sí menos
        mensaje = str(mensaje, "utf8") # Convertir los bytes a caracteres
        if mensaje == "":
            break

        # Segundo, quitarle el "fin de línea" que son sus 2 últimos caracteres
        linea = mensaje[:-2]  # slice desde el principio hasta el final -2

        # Tercero, darle la vuelta
        linea = linea[::-1]

        #imprimir la respuesta en pantalla
        print("Se ha recibido un datagrama desde", dir)
        print("Contiene lo siguiente: ")
        print(f"{linea}")

        # Finalmente, enviarle la respuesta con un fin de línea añadido
        # Observa la transformación en bytes para enviarlo
        sd.sendall(bytes(linea+"\r\n", "utf8"))
    print(f"El cliente {dir} ha cerrado la conexión.")
    sd.close()  # Cerrar el socket del cliente