calificaciones = {}

while (True):
    print("\nOpciones:" "\n"
    "1. Registrar un alumno" "\n"
    "2. Registrar calificación" "\n"
    "3. Mostrar calificaciones" "\n"
    "4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre in calificaciones:
            print("El alumno ya está registrado.")
            continue
        else:
            calificaciones[nombre] = {}
            print("Alumno registrado.")
        
    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno: ")
        if nombre not in calificaciones:
            print("El alumno no está registrado.")
            continue
        else:
            while True:
                materia = input("Ingrese la materia (o 'salir' para terminar): ")
                if materia.lower() == 'salir':
                    break
                calificacion = input(f"Ingrese la calificación para {materia}: ")
                calificaciones[nombre][materia] = calificacion
                print("Calificaciones registradas.")

    elif opcion == "3":
        for i in calificaciones:
            print(f"Alumno: {i}, Calificación: {calificaciones[i]}")
    elif opcion == "4":
        print("Saliendo del programa.")
        break