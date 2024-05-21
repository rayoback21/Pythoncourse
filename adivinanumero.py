import random

# Programa que genera un número aleatorio y permite al usuario adivinarlo
def adivina_el_numero():
    numero_aleatorio = random.randint(1, 100)
    adivinado = False

    while not adivinado:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento < numero_aleatorio:
            print("Demasiado bajo")
        elif intento > numero_aleatorio:
            print("Demasiado alto")
        else:
            print("¡Correcto! Has adivinado el número.")
            adivinado = True

adivina_el_numero()
