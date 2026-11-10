
import paramiko
import time

client = paramiko.SSHClient()


client.connect(
    'localhost',
    username='uo296168',
    password='clave-mal'
)

print("Conectado!!")

# Ejecutar un comando remoto
stdin, stdout, stderr = client.exec_command('ls')

# Mostrar el resultado
for line in stdout:
    print(line.rstrip())

time.sleep(1)
client.close()
