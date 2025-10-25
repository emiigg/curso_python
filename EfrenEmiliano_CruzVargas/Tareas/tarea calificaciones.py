
calificaciones = {}

while True:
    # Mostrar menú
    print("\n=== MENÚ DE CALIFICACIONES ===")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")
    
    opcion = input("Selecciona una opción (1-4): ")
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ").strip()
        if nombre in calificaciones:
            print("El alumno ya existe.")
        else:
            calificaciones[nombre] = {}
            print("Alumno registrado correctamente.")
    
    elif opcion == "2":
        nombre = input("Ingresa el nombre del alumno: ").strip()
        if nombre not in calificaciones:
            print("Alumno no encontrado.")
        else:
            print("Ingresa 'salir' para terminar de registrar materias.")
            while True:
                materia = input("Ingresa el nombre de la materia: ").strip()
                if materia.lower() == "salir":
                    break
                
                try:
                    calificacion = float(input(f"Ingresa la calificación para {materia}: "))
                    calificaciones[nombre][materia] = calificacion
                    print(f"Calificación de {materia} registrada correctamente.")
                except ValueError:
                    print("Error: La calificación debe ser un número.")
    
    elif opcion == "3":
        if not calificaciones:
            print("No hay alumnos registrados.")
        else:
            print("\n=== CALIFICACIONES DE TODOS LOS ALUMNOS ===")
            for alumno, materias in calificaciones.items():
                print(f"\n{alumno}:")
                if not materias:
                    print("  No tiene calificaciones registradas.")
                else:
                    suma_calificaciones = 0
                    for materia, calificacion in materias.items():
                        print(f"  {materia}: {calificacion}")
                        suma_calificaciones += calificacion
                    
                    # Calcular y mostrar promedio
                    promedio = suma_calificaciones / len(materias)
                    print(f"  Promedio: {promedio:.2f}")
    
    # Opción 4: Salir
    elif opcion == "4":
        print("...")
        print("Terminando programa...")
        print("...")
        print("Programa Finalzado")
        break
    
    # Opción inválida
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")