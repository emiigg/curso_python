# Diccionario principal
calificaciones = {}

while True:
    # Mostrar menu
    print("\n=== MENU DE CALIFICACIONES ===")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")
    
    opcion = input("Elige una opcion: ")

    # Opcion 1: Registrar nuevo alumno
    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        if nombre in calificaciones:
            print("El alumno ya esta registrado.")
        else:
            calificaciones[nombre] = {}
            print("Alumno registrado correctamente.")

    # Opcion 2: Registrar calificaciones para un alumno
    elif opcion == "2":
        nombre = input("Ingresa el nombre del alumno: ")
        if nombre not in calificaciones:
            print("Alumno no encontrado.")
        else:
            while True:
                materia = input("Ingresa la materia (o 'salir' para terminar): ")
                if materia.lower() == "salir":
                    break
                try:
                    calificacion = float(input("Ingresa la calificacion: "))
                    calificaciones[nombre][materia] = calificacion
                except ValueError:
                    print("Por favor, ingresa un numero valido para la calificacion.")

    # Opcion 3: Mostrar todas las calificaciones
    elif opcion == "3":
        if not calificaciones:
            print("No hay alumnos registrados.")
        else:
            for alumno, materias in calificaciones.items():
                print(f"\n{alumno}:")
                if materias:
                    suma = 0
                    for mat, cal in materias.items():
                        print(f"  {mat}: {cal}")
                        suma += cal
                    promedio = suma / len(materias)
                    print(f"  Promedio: {promedio:.2f}")
                else:
                    print("  No hay calificaciones registradas.")

    # Opcion 4: Salir
    elif opcion == "4":
        print("Hasta luego!")
        break

    else:
        print("Opcion invalida, intenta de nuevo.")
