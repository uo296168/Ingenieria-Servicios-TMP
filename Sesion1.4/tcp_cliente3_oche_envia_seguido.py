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
    
    # 1. Pedimos los inputs ANTES de conectar para no perder tiempo luego
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

    # 2. AHORA nos conectamos. El servidor hace accept() y se duerme 1 segundo.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, puerto)) 

    # 3. Disparamos los 3 mensajes de golpe. Como el servidor duerme, se acumulan en su red.
    for m in mensajes_pendientes: 
        s.sendall(m.encode()) 

    respuestas_recibidas = []
    buffer_str = ""

    # 4. Leemos hasta tener exactamente 3 respuestas limpias
    while len(respuestas_recibidas) < 3:
        data = s.recv(1024)
        if not data:
            break
        
        buffer_str += str(data, "utf8")
        buffer_str = buffer_str.replace("\n\r", "\r\n")
        
        while "\r\n" in buffer_str:
            mensaje_completo, buffer_str = buffer_str.split("\r\n", 1)
            respuestas_recibidas.append(mensaje_completo)

    # 5. El servidor nos devolvió todo el bloque invertido (orden 3, 2, 1).
    # Le damos la vuelta a la lista para ordenarlo 1, 2, 3 visualmente.
    respuestas_recibidas.reverse() # patatinha

    for r in respuestas_recibidas:
        print(f"Respuesta recibida: {r}")

    s.close()
print("Cerrando la conexión de este bloque...\n") 