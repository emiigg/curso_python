calificaciones = {}

while True:
    print("\n=== MENÚ DE CALIFICACIONES ===")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("\nIngresa el nombre del alumno: ").strip()
        if nombre in calificaciones:
            print("El alumno ya está registrado.")
        else:
            calificaciones[nombre] = {}
            print("Alumno registrado correctamente.")

    elif opcion == "2":
        nombre = input("\nIngresa el nombre del alumno: ").strip()
        if nombre not in calificaciones:
            print("Alumno no encontrado.")
        else:
            while True:
                materia = input("Ingresa la materia (o 'salir' para terminar): ").strip()
                if materia.lower() == "salir":
                    break
                try:
                    calificacion = float(input("Ingresa la calificación: "))
                    calificaciones[nombre][materia] = calificacion
                except ValueError:
                    print("Error: Ingresa un número válido para la calificación.")

    elif opcion == "3":
        if not calificaciones:
            print("\nNo hay alumnos registrados.")
        else:
            print("\n=== CALIFICACIONES REGISTRADAS ===")
            for alumno, materias in calificaciones.items():
                print(f"\n{alumno}:")
                if materias:
                    total = 0
                    for materia, calificacion in materias.items():
                        print(f"  {materia}: {calificacion}")
                        total += calificacion
                    promedio = total / len(materias)
                    print(f"  Promedio: {promedio:.2f}")
                else:
                    print("  (Sin materias registradas)")

    elif opcion == "4":
        print("\nSaliendo del programa... ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")