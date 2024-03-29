#Proyecto de introducción a la programación.
#Valeria Calvo,Joseph Mora, Brayan Jiménez.
#Se le pide al usuario que agregue las especificaciones de las tareas
#Se genera una lista de tareas para almacenarlas.
tareas = []

# Función para agregar una nueva tarea
def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha = input("Ingrese la fecha de la tarea (dd/mm/aaaa): ")
    costo = float(input("Ingrese el costo de la tarea: $"))
    completada = False
    nueva_tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'fecha': fecha,
        'costo': costo,
        'completada': completada
    }
    tareas.append(nueva_tarea)
    print("Tarea agregada con éxito.")

# Función para ver las tareas pendientes o completadas
def ver_tareas(completadas=False):
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas, start=1):
        if tarea['completada'] == completadas:
            estado = 'Completada' if tarea['completada'] else 'Pendiente'
            print(f"{i}. Título: {tarea['titulo']} - Descripción: {tarea['descripcion']} - Fecha: {tarea['fecha']} - Costo: ${tarea['costo']} - Estado: {estado}")

# Función para marcar una tarea como completada
def marcar_completada():
    ver_tareas()
    num_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
    if 1 <= num_tarea <= len(tareas):
        tareas[num_tarea - 1]['completada'] = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

# Función para editar una tarea
def editar_tarea():
    ver_tareas()
    num_tarea = int(input("Ingrese el número de la tarea que desea editar: "))
    if 1 <= num_tarea <= len(tareas):
        tarea = tareas[num_tarea - 1]
        tarea['titulo'] = input("Ingrese el nuevo título de la tarea: ")
        tarea['descripcion'] = input("Ingrese la nueva descripción de la tarea: ")
        tarea['fecha'] = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
        tarea['costo'] = float(input("Ingrese el nuevo costo de la tarea: $"))
        print("Tarea editada con éxito.")
    else:
        print("Número de tarea inválido.")

# Función para borrar una tarea
def borrar_tarea():
    ver_tareas()
    num_tarea = int(input("Ingrese el número de la tarea que desea borrar: "))
    if 1 <= num_tarea <= len(tareas):
        del tareas[num_tarea - 1]
        print("Tarea borrada con éxito.")
    else:
        print("Número de tarea inválido.")

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Ver Tareas Completadas")
    print("4. Marcar Tarea como Completada")
    print("5. Editar Tarea")
    print("6. Borrar Tarea")
    print("7. Salir")

    opcion = input("Seleccione una opción (1-7): ")

    if opcion == '1':
        agregar_tarea()
    elif opcion == '2':
        ver_tareas(completadas=False)
    elif opcion == '3':
        ver_tareas(completadas=True)
    elif opcion == '4':
        marcar_completada()
    elif opcion == '5':
        editar_tarea()
    elif opcion == '6':
        borrar_tarea()
    elif opcion == '7':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del 1 al 7.")

     
