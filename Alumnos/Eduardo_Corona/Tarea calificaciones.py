calificaciones = {}

while True:
    print("\nMenú de calificaciones")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")

    opcion = input("Elige una opción (1, 2, 3, 4): ")

    if opcion == "1":
        nombre = input("Nombre del alumno: ")
        calificaciones[nombre] = {}
        print("Alumno registrado correctamente")

    elif opcion == "2":
        nombre = input("Nombre del alumno: ")
        if nombre in calificaciones:
            materia = input("Materia: ")
            calificacion = input("Calificación: ")
            calificaciones[nombre][materia] = calificacion
            print("Calificación registrada.")
        else:
            print("El alumno no está registrado")

    elif opcion == "3":
        if calificaciones:
            for alumno, materias in calificaciones.items():
                print(f"\nAlumno: {alumno}")
                for materia, calificacion in materias.items():
                    print(f" {materia}: {calificacion}")
        else:
            print("No hay alumnos registrados.")

    elif opcion == "4":
        print("Saliendo")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")