import socket
import sys

if len(sys.argv) != 3:
    print("Usando el puerto 9999 por defecto e ip localhost")
    puerto = 9999
    ip = "localhost"
else:
    puerto = int(sys.argv[1])
    ip = sys.argv[2]

while True: 
    mensajes_pendientes = [] 
    
    for i in range(3): 
        msg = input(f"Introduce mensaje {i+1}/3 (debe acabar en \\r\\n, vacio para salir): ") 
        if msg == "": 
            break 
            
        if msg[-4:] != "\\r\\n": 
            msg = msg + "\\r\\n"
        msg_real = msg.replace("\\r\\n", "\r\n") 
        mensajes_pendientes.append(msg_real) 

    if len(mensajes_pendientes) < 3: 
        break 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, puerto)) 

    for m in mensajes_pendientes: 
        s.sendall(m.encode("utf8")) 

    respuestas_recibidas = []
    
    # Convertimos el socket en un fichero para lectura
    f = s.makefile(encoding="utf8", newline="\r\n")

    for _ in range(3):
        mensaje = f.readline()
        if not mensaje:
            break
            
        mensaje_completo = mensaje[:-2] # Quitamos el \r\n
        respuestas_recibidas.append(mensaje_completo)

    respuestas_recibidas.reverse()

    for r in respuestas_recibidas:
        print(f"Respuesta recibida: {r}")

    f.close()
    s.close()
    print("Cerrando la conexión de este bloque...\n")