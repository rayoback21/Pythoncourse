
def mostrar_tareas(tareas):
    print("\nLista de tareas:")
    for i, tarea in enumerate(tareas, start=1):
        print(f"{i}. {tarea}")
    print()

def agregar_tarea(tareas):
    tarea = input("Ingresa la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    numero_tarea = int(input("Ingresa el número de la tarea a eliminar: "))
    if 0 < numero_tarea <= len(tareas):
        tareas.pop(numero_tarea - 1)
        print("Tarea eliminada.")
    else:
        print("Número de tarea inválido.")

def main():
    tareas = []
    while True:
        print("1. Mostrar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

main()
