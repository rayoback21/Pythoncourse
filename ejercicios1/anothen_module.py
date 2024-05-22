# Programa que cuenta el número de palabras en una cadena de texto dada
def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = input("Ingresa una cadena de texto: ")
numero_palabras = contar_palabras(texto)
print(f"Número de palabras: {numero_palabras}")
