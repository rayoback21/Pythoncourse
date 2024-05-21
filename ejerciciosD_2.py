def leer_colaboradores(archivo):
  """
  Función que lee el contenido de un archivo de texto y lo devuelve como una lista de colaboradores, eliminando "NUEVO COLABORADOR".

  Parámetros:
    archivo (str): La ruta del archivo de texto.

  Devuelve:
    list: Una lista de colaboradores (nombres en mayúsculas).
  """
  colaboradores = []
  with open(archivo, 'r') as f:
    for colaborador in f.readlines():
      colaborador = colaborador.strip().upper()
      if colaborador != "NUEVO COLABORADOR":
        colaboradores.append(colaborador)
  return colaboradores


def mostrar_colaboradores(colaboradores):
  """
  Función que muestra en pantalla los colaboradores de una lista.

  Parámetros:
    colaboradores (list): La lista de colaboradores.
  """
  print("\n**Listado de colaboradores:**")
  for i, colaborador in enumerate(colaboradores):
    print(f"{i + 1}. {colaborador}")


def agregar_colaborador(colaboradores, archivo, nuevo_colaborador):
  """
  Función que agrega un nuevo colaborador al archivo de texto.

  Parámetros:
    colaboradores (list): La lista de colaboradores en memoria.
    archivo (str): La ruta del archivo de texto.
    nuevo_colaborador (str): El nombre del nuevo colaborador (en mayúsculas).
  """
  if len(colaboradores) >= 15:
    print("Error: No se pueden agregar más de 15 colaboradores.")
    return

  if nuevo_colaborador.upper() in colaboradores:
    print(f"Error: El colaborador '{nuevo_colaborador}' ya existe.")
    return

  colaboradores.append(nuevo_colaborador.upper())

  with open(archivo, 'a') as f:
    f.write(f"{nuevo_colaborador}\n")

  print(f"El colaborador '{nuevo_colaborador}' se ha agregado exitosamente al archivo.")


def main():
  """Función principal del programa."""
  archivo = 'colaboradores.txt'
  colaboradores = leer_colaboradores(archivo)

  # Mostrar los colaboradores iniciales
  mostrar_colaboradores(colaboradores)

  # Agregar colaboradores uno por uno
  while True:
    opcion = input("\n¿Desea agregar un nuevo colaborador? (s/n): ").lower()
    if opcion != 's' and opcion != 'n':
      print("Opción no válida. Ingrese 's' para agregar o 'n' para salir.")
      continue

    if opcion == 'n':
      break

    nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador: ").upper()
    agregar_colaborador(colaboradores, archivo, nuevo_colaborador)

    # Mostrar el nuevo colaborador agregado
    mostrar_colaboradores(colaboradores)


if __name__ == "__main__":
  main()
