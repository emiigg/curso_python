calificaciones = {}


while True:
    print("\nOpciones:")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")
    opcion = input("Selecciona una opción (1, 2, 3, 4): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del alumno: ")
        calificaciones[nombre] = {}
        print("Alumno registrado correctamente")

    elif opcion == "2":
        nombre = input("Ingresa el nombre del alumno: ")
        if nombre not in calificaciones:
            print("Alumno no encontrado.")
        else:
            print("Registrando calificaciones para " + nombre)
            while True:
                materia = input("Nombre de la materia: ")
                if materia == "salir":
                    break
                calif_mat = float(input(f"Calificación para '{materia}': "))
                
                # Esta línea tenía indentación extra
                calificaciones[nombre][materia] = calif_mat
                
            # Moví esta línea para que solo se muestre una vez al salir
            print("Calificacion registrada correctamente")

    elif opcion == "3":
        print("LISTA DE CALIFICACIONES")
        
        
        if not calificaciones:
            print("No hay alumnos registrados todavía.")
        
        # Recorremos las claves (nombres) del diccionario principal
        for nombre in calificaciones:
            
            print(f"\nAlumno: {nombre}")
            
            # Accedemos al diccionario anidado usando la clave (nombre)
            # Sintaxis: materias_dict = calificaciones[nombre]
            # Esto es como hacer: emiliano_info = personas["Emiliano"]
            materias_dict = calificaciones[nombre]                                                                           
            
            total_calificaciones = 0
            num_materias = 0
            
            for materia in materias_dict:
                
                # Accedemos al valor final (calificación) usando la clave anidada
                # Sintaxis: calificacion = materias_dict[materia]
                # Esto es como hacer: ciudad_ana = personas["Ana"]["ciudad"]
                calificacion = materias_dict[materia] 
                
                print({materia}  + ":"  + {calificacion})
                total_calificaciones += calificacion
                num_materias += 1
                promedio = total_calificaciones / num_materias
            print(f"  Promedio: " + promedio)
    elif opcion == "4":
         print("Saliendo")
         break
    else: 
        print("Opción no válida. Intenta de nuevo.")