
import dns.resolver

# Consultamos la dirección IPv4 de Wikipedia
respuesta = dns.resolver.resolve("en.wikipedia.org", "A")

# Mostramos la primera dirección IP obtenida
print(respuesta[0].address)

# Mostramos la respuesta DNS completa
print(respuesta.response)

# Mostramos la respuesta en formato binario
print(respuesta.response.to_wire())