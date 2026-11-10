
import paramiko
import time
import getpass
import base64

client = paramiko.SSHClient()

client = paramiko.SSHClient()

key = paramiko.Ed25519Key(
    data=base64.b64decode(b'AAAAC3NzaC1lZDI1NTE5AAAAIJphQN4S3+QoKO5CgEB7Z++Ys8LxcgUkxIYGbQ/Ym4t7') 
)

client.get_host_keys().add('localhost', 'ssh-ed25519', key) #insertamos la clave publica del servidor especifico

clave = getpass.getpass("Contraseña de Ubuntu: ") #pedimos la contraseña de forma segura sin mostrarla en pantalla

client.connect(
    'localhost',
    username='uo296168',
    password=clave,
    look_for_keys=False, #desactiva la búsqueda de claves SSH en el sistema
    allow_agent=False #desactiva el uso del agente SSH para la autenticación
)

print("Conectado!!")

# Ejecutar un comando remoto
stdin, stdout, stderr = client.exec_command('ls')

# Abrimos una sesión SFTP sobre la conexión SSH
sftp = client.open_sftp()

# Obtenemos los archivos de la carpeta personal remota
archivos = sftp.listdir()

print("Contenido de la carpeta remota:")

for archivo in archivos:
    print(archivo)

# Cerramos la sesión SFTP
sftp.close()

time.sleep(1)
client.close()