calificaciones = {}

while True:
    print("\n=== MENU DE CALIFICACIONES ===")
    print("1. Registrar nuevo alumno")
    print("2. Registrar/Actualizar calificacion para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")
    opcion = input("Selecciona una opcion (1, 2, 3, 4): ")

    if opcion == "1":
        alumno = input("Ingresa el nombre del alumno: ")
        if alumno in calificaciones:
            print(f"El alumno '{alumno}' ya esta registrado.")
        else:
            calificaciones[alumno] = {}
            print(f"Alumno '{alumno}' agregado.")

    elif opcion == "2":
        alumno = input("Ingresa el nombre del alumno: ")
        if alumno not in calificaciones:
            print(f"El alumno '{alumno}' no se encuentra en la lista. Regístralo primero en la opción 1.")
        else:
            materia = input("Ingresa la materia: ")
            calificacion = int(input("Ingresa la calificacion (0-100): "))
            while calificacion < 0 or calificacion > 100:
                print("La calificacion debe ser de 0 a 100. Intenta de nuevo.")
                calificacion = int(input("Ingresa la calificacion: "))
            calificaciones[alumno][materia] = calificacion
            print(f"Calificación de '{alumno}' en '{materia}': {calificacion} pts.")

    elif opcion == "3":
        if calificaciones:
            print("\n=== Todas las Calificaciones ===")
            for alumno, materias in calificaciones.items():
                print(f"\n{alumno}:")
                if materias:
                    for materia, calificacion in materias.items():
                        print(f"  {materia}: {calificacion}")
                else:
                    print("  (sin materias registradas)")
        else:
            print("No hay calificaciones aún.")

    elif opcion == "4":
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
