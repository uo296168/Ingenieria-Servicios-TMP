
import paramiko
import time
import getpass

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.WarningPolicy()) #aceptamos la clave publica del servidor sin verificar su identidad pero mostramos una advertencia

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

# Mostrar el resultado
for line in stdout:
    print(line.rstrip())

time.sleep(1)
client.close()