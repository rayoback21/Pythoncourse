# Programa que realiza operaciones básicas de una calculadora
def calculadora(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "División por cero no permitida"
    return suma, resta, multiplicacion, division

# Entradas del usuario
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

resultados = calculadora(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
