# Lista global que almacenará los estudiantes registrados
estudiantes = []

def menu():
    """
    Esta función muestra el menú principal del sistema.
    Permite al usuario seleccionar entre diferentes opciones.
    """
    print("\nBienvenido al Sistema de Registro de Matrículas")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_estudiante():
    """
    Esta función permite registrar un nuevo estudiante en el sistema.
    Pide al usuario ingresar el nombre y la edad del estudiante, y lo añade a la lista global 'estudiantes'.
    """
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    estudiante = {'nombre': nombre, 'edad': edad}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")

def mostrar_estudiantes():
    """
    Esta función muestra la lista de estudiantes registrados.
    Si no hay estudiantes registrados, informa al usuario.
    """
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return None
    
    print("Lista de estudiantes registrados:")
    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"{i}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
    return estudiantes

def actualizar_estudiante():
    """
    Esta función permite actualizar la información de un estudiante existente.
    Muestra una lista numerada de estudiantes y permite al usuario elegir cuál actualizar.
    """
    estudiantes_list = mostrar_estudiantes()
    if estudiantes_list is None:
        return

    try:
        seleccion = int(input("Selecciona el número del estudiante que deseas actualizar: "))
        if 1 <= seleccion <= len(estudiantes_list):
            estudiante = estudiantes_list[seleccion - 1]
            nombre_actual = estudiante['nombre']
            print(f"Estudiante encontrado: {nombre_actual}")
            nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter para no cambiarlo): ")
            nueva_edad = input("Ingresa la nueva edad (o presiona Enter para no cambiarla): ")

            if nuevo_nombre:
                estudiante['nombre'] = nuevo_nombre
            if nueva_edad:
                estudiante['edad'] = int(nueva_edad)

            print(f"Estudiante {nombre_actual} actualizado con éxito.")
        else:
            print("Número no válido.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

def eliminar_estudiante():
    """
    Esta función permite eliminar a un estudiante del sistema.
    Muestra una lista numerada de estudiantes y permite al usuario elegir cuál eliminar.
    """
    estudiantes_list = mostrar_estudiantes()
    if estudiantes_list is None:
        return

    try:
        seleccion = int(input("Selecciona el número del estudiante que deseas eliminar: "))
        if 1 <= seleccion <= len(estudiantes_list):
            estudiante = estudiantes_list[seleccion - 1]
            nombre = estudiante['nombre']
            estudiantes.remove(estudiante)
            print(f"Estudiante {nombre} eliminado con éxito.")
        else:
            print("Número no válido.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

def main():
    """
    Función principal que controla el flujo del programa.
    Usa un bucle while para mostrar el menú y realizar las acciones según la elección del usuario.
    """
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            actualizar_estudiante()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutamos la función principal para iniciar el programa
main()

                                         