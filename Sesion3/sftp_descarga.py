
import paramiko
import time
import getpass
import base64
from stat import S_ISREG
from pathlib import Path
import posixpath

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


# Abrimos la conexión SFTP
sftp = client.open_sftp()

# Carpeta remota que queremos descargar
carpeta_remota = "/home/uo296168/sftp_pruebas"

# Carpeta local donde guardaremos los archivos
carpeta_local = Path(__file__).resolve().parent / "descargas_sftp"
carpeta_local.mkdir(exist_ok=True) #Si no existe la crea

# Obtenemos los nombres de la carpeta remota
archivos = sftp.listdir(carpeta_remota)

for archivo in archivos:

    ruta_remota = posixpath.join(carpeta_remota, archivo) #Acceso al archivo que queremos descargar
    ruta_local = carpeta_local / archivo #ruta donde descargaremos el archivo

    # Consultamos los atributos del archivo
    datos = sftp.stat(ruta_remota)

    # Descargamos únicamente archivos regulares
    if S_ISREG(datos.st_mode):
        sftp.get(ruta_remota, str(ruta_local)) 
        print(f"Descargado: {archivo}")
    else:
        print(f"Ignorado (no es archivo regular): {archivo}")

sftp.close()

print("Contenido de la carpeta remota:")

for archivo in archivos:
    print(archivo)

# Cerramos la sesión SFTP
sftp.close()

time.sleep(1)
client.close()