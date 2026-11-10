import dns.resolver

# Consultamos las direcciones IPv4 de Apple
respuesta = dns.resolver.resolve("apple.com", "A")

# Recorremos todas las direcciones IP obtenidas
for registro in respuesta:
    print(registro.address)