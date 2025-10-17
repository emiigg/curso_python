calificaciones = {}

while True:
    print("\n---MENÚ DE CALIFICACIONES---")
    print("1.Registrar alumno")
    print("2.Registrar calificaciones para un alumno")
    print("3.Mostrar todas las calificaciones")
    print("4.Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n---Registro de alumno---")
        nombre = input("Ingrese el nombre del alumno: ")
        calificaciones[nombre] = {}
        print(f"Alumno {nombre} registrado correctamente")
        
    elif opcion=="2":
        print("\n---Registro de calificaciones para un alumno---")
        alumno = input("Ingrese el nombre del alumno: ")
        
        if alumno in calificaciones:
            while True:
                materia = input("Ingrese el nombre de la materia: ")
                calificacion = float(input("Ingrese la calificación: "))
                calificaciones[alumno][materia] = calificacion

                subOpcion = input("Escriba 'salir' si no desea registrar otra materia (o cualquier otra cosa para continuar): ")
                if subOpcion == "salir" or subOpcion == "Salir":
                    break
                else:
                    print("Se registrará otra materia...")
        else:
            print("Alumno no encontrado")
    
    elif opcion == "3":
        if calificaciones:
            print("\n---Diccionario de los alumnos, materias y sus calificaciones---")
            
            for nombre, materias in calificaciones.items():
                print(f"\nAlumno: {nombre}")
                suma = 0
                n = 0
                for materia, calificacion in materias.items():
                    print(f"{materia} = {calificacion}")
                    suma += calificacion
                    n += 1
                if n > 0:
                    print(f"Promedio: {suma/n}")
                else:
                    print("Sin materias registradas")
        else:
            print("Diccionario vacío")
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")            