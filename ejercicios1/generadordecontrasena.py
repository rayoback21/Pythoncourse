import random
import string

# Programa que genera una contraseña aleatoria
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = int(input("Ingresa la longitud de la contraseña: "))
contrasena = generar_contrasena(longitud)
print(f"Contraseña generada: {contrasena}")
