while (True):
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        agenda[nombre] = telefono

    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        encontrado = False
        with open("agenda.txt", "r") as archivo:
            for linea in archivo:
                nombre, telefono = linea.strip().split(",")
                if nombre == nombre_buscar:
                    print(f"Contacto encontrado: {nombre} - {telefono}")
                    encontrado = True
                    break
        if not encontrado:
            print("Contacto no encontrado.")

    elif opcion == "3":
        if agenda:
            print("Contactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        

    elif opcion == "4":
        print("Saliendo de la agenda.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")