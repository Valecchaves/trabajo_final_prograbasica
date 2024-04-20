# Función cargar las tareas desde un archivo
def cargar_tareas():
    tareas = []  # Inicializar la lista de tareas
    try:
        with open("Tareas.txt", "r") as archivo:
            for linea in archivo:
                tarea = linea.strip().split('|')
                nueva_tarea = {
                    'titulo': tarea[0],
                    'descripcion': tarea[1],
                    'fecha': tarea[2],
                    'costo': float(tarea[3]),
                    'completada': tarea[4] == 'True'
                }
                tareas.append(nueva_tarea)
    except FileNotFoundError:
        print("El archivo de tareas no se encontró. Se creará uno nuevo al agregar tareas.")
        # Si el archivo no existe, retornamos la lista vacía de tareas
    return tareas

# Función guardar las tareas en un archivo
def guardar_tareas(tareas):
    with open("Tareas.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['titulo']}|{tarea['descripcion']}|{tarea['fecha']}|{tarea['costo']}|{tarea['completada']}\n")

# Función agregar una nueva tarea
def agregar_tarea():
    print("Agregar nueva tarea:")
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha = input("Ingrese la fecha de la tarea (dd/mm/aaaa): ")
    costo = float(input("Ingrese el costo de la tarea: $"))
    completada = False
    nueva_tarea = {'titulo': titulo, 'descripcion': descripcion, 'fecha': fecha, 'costo': costo, 'completada': completada}
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print("Tarea agregada con éxito.")
#Función ver las tareas pendientes o completadas
def ver_tareas(completadas=False):
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas, start=1):
        if tarea['completada'] == completadas:
            estado = 'Completada' if tarea['completada'] else 'Pendiente'
            print(f"{i}. Título: {tarea['titulo']} - Descripción: {tarea['descripcion']} - Fecha: {tarea['fecha']} - Costo: ${tarea['costo']} - Estado: {estado}")

# Función marcar una tarea como completada
def marcar_completada():
    ver_tareas()
    num_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
    if 1 <= num_tarea <= len(tareas):
        tareas[num_tarea - 1]['completada'] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")

# Función editor una tarea
def editar_tarea():
    ver_tareas()
    num_tarea = int(input("Ingrese el número de la tarea que desea editar: "))
    if 1 <= num_tarea <= len(tareas):
        tarea = tareas[num_tarea - 1]
        tarea['titulo'] = input("Ingrese el nuevo título de la tarea: ")
        tarea['descripcion'] = input("Ingrese la nueva descripción de la tarea: ")
        tarea['fecha'] = input("Ingrese la nueva fecha de la tarea (dd/mm/aaaa): ")
        tarea['costo'] = float(input("Ingrese el nuevo costo de la tarea: $"))
        guardar_tareas(tareas)
        print("Tarea editada con éxito.")
    else:
        print("Número de tarea inválido.")

# Función borrar una tarea
def borrar_tarea():
    ver_tareas()
    num_tarea = int(input("Ingrese el número de la tarea que desea borrar: "))
    if 1 <= num_tarea <= len(tareas):
        del tareas[num_tarea - 1]
        guardar_tareas(tareas)
        print("Tarea borrada con éxito.")
    else:
        print("Número de tarea inválido.")

# Función proporcionar estadísticas básicas de las tareas
def estadisticas():
    total_tareas = len(tareas)
    total_pendientes = sum(1 for tarea in tareas if not tarea['completada'])
    total_completadas = sum(1 for tarea in tareas if tarea['completada'])
    costo_pendientes = sum(tarea['costo'] for tarea in tareas if not tarea['completada'])
    costo_completadas = sum(tarea['costo'] for tarea in tareas if tarea['completada'])
    costo_total = costo_pendientes + costo_completadas

    print("\nEstadísticas:")
    print(f"Número total de tareas: {total_tareas}")
    print(f"Número total de tareas pendientes: {total_pendientes}")
    print(f"Número total de tareas completadas: {total_completadas}")
    print(f"Total del coste ($) de tareas pendientes: ${costo_pendientes}")
    print(f"Total del coste ($) de tareas completadas: ${costo_completadas}")
    print(f"Costo total ($) de todas las tareas: ${costo_total}")

# Función mostrar el cronograma de tareas pendientes ordenadas por fecha
def obtener_fecha(tarea):
    return tarea['fecha']

def cronograma_pendientes():
    tareas_pendientes = [tarea for tarea in tareas if not tarea['completada']]
    if tareas_pendientes:
        tareas_pendientes_ordenadas = sorted(tareas_pendientes, key=obtener_fecha)
        print("\nCronograma de Tareas Pendientes:")
        for i, tarea in enumerate(tareas_pendientes_ordenadas, start=1):
            print(f"{i}. Título: {tarea['titulo']} - Fecha: {tarea['fecha']}")
    else:
        print("\nNo hay tareas pendientes.")
# Cargar las tareas desde el archivo al iniciar el programa
tareas = cargar_tareas()

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Ver Tareas Completadas")
    print("4. Marcar Tarea como Completada")
    print("5. Editar Tarea")
    print("6. Borrar Tarea")
    print("7. Estadísticas")
    print("8. Cronograma de Tareas Pendientes")
    print("9. Salir")

    opcion = input("Seleccione una opción (1-9): ")

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
        estadisticas()
    elif opcion == '8':
        cronograma_pendientes()
    elif opcion == '9':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del 1 al 9.")





