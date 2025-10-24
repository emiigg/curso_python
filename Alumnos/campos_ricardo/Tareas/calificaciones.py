# === MENÚ DE CALIFICACIONES ===

alumnos = {}

while True:
    print("\n=== MENÚ DE CALIFICACIONES ===")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("\nIngresa el nombre del alumno: ")
        if nombre in alumnos:
            print("El alumno ya está registrado.")
        else:
            alumnos[nombre] = {}
            print("Alumno registrado correctamente.")

    elif opcion == "2":
        nombre = input("\nIngresa el nombre del alumno: ")
        if nombre not in alumnos:
            print("El alumno no está registrado.")
        else:
            while True:
                materia = input("Ingresa la materia (o 'salir' para terminar): ")
                if materia.lower() == "salir":
                    break
                try:
                    calificacion = float(input("Ingresa la calificación: "))
                    alumnos[nombre][materia] = calificacion
                except ValueError:
                    print("Por favor ingresa un número válido.")

    elif opcion == "3":
        if not alumnos:
            print("\nNo hay alumnos registrados.")
        else:
            for nombre, materias in alumnos.items():
                print(f"\n{nombre}:")
                if materias:
                    total = 0
                    for materia, calificacion in materias.items():
                        print(f"  {materia}: {calificacion}")
                        total += calificacion
                    promedio = total / len(materias)
                    print(f"  Promedio: {promedio:.1f}")
                else:
                    print("  Sin calificaciones registradas.")
    
    elif opcion == "4":
        print("\nSaliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
