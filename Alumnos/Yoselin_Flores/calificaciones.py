calificaciones = {}

while True:
    print("Menú de calificaciones")
    print("1. Registrar un nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostrar todas las calificaciones")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Ingresar el nombre del alumno: ")
        if nombre in calificaciones:
                print("Ese alumno ya existe. ")
        else:
             calificaciones[nombre] = {}
             print("Alumno registrado correctamente")

    elif opcion == "2":
         nombre = input("Ingresar el nombre del alumno: ")
         if nombre not in calificaciones:
              print("Lo siento, alumno no encontrado")
         else:
            while True:
                  materia = input("ingresar la materia o dale en salir para terminar: ")
                  if materia.lower() == "salir.":
                        break
                  calificacion = float(input("ingresar la calificacion"))
                  calificaciones[nombre][materia] = calificacion
            print("Ok, calificaciones registradas correctamente")
    
    elif opcion == "3":
        if not calificaciones:
             print("Lo siento, no hay alumno registrado")
        else:
             for alumno, materias in calificaciones.items():
                  print(("/n{alumno}:"))
                  total = 0
                  for materia, calificacion in materias.items():
                       print("{materia}: {calificacion}")
                       total == calificacion
                  if materias:
                   promedio = total / len(materias)
                  print(("promedio: {promedio: .2f}"))
    
    
    elif opcion == "4":
         print("Operacion finalizada")
         break
    
    else:
         print("opcion no valida, intentar de nuevo. ")


                  


