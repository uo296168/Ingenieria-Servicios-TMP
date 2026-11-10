
import dns.resolver

# Consultamos los registros MX de Gmail
respuesta = dns.resolver.resolve("gmail.com", "MX")

# Ordenamos los servidores por prioridad
servidores = sorted(respuesta, key=lambda registro: registro.preference)

# Recorremos los servidores de correo
for servidor in servidores:

    prioridad = servidor.preference
    nombre = str(servidor.exchange)

    # Consultamos las direcciones IPv4 del servidor
    direcciones = dns.resolver.resolve(nombre, "A")

    for direccion in direcciones:
        print(prioridad, nombre, direccion.address)
