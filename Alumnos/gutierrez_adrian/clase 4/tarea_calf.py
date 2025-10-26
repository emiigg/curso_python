calificaciones = {}

while True:
    print("\nMenú de calificaciones")
    print("1. Registrar nuevo alumno")
    print("2. Registrar calificaciones para un alumno")
    print("3. Mostar todas las calificaciones guardadas")
    print("4. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del nuevo alumno: ")
        calificaciones[nombre] = {}
    elif opcion == "2":
        nombre = input("Ingresa el nombre del alumno: ")
        if nombre not in calificaciones:
            print("Alumno no encontrado")
        else:
            while True:
                materia = input("Escribe la materia o salir para termianr: ")
                if materia.lower() == "salir":
                    break
                calificacion = int(input("Ingrese la calificacion en base 100: "))
                calificaciones[nombre][materia] = calificacion
                print("las calificacions han sido registradas")
    
    elif opcion == "3":
        for alumno, materias in calificaciones.items():
            print(f"\n{alumno}: ")
            total = 0
            for materia, calificacion in materias.items():
                print(f" {materia}: {calificacion}")
                total += calificacion
            if materias:
                promedio = total/len(materias)
                print(f"Promedio: {promedio}")
