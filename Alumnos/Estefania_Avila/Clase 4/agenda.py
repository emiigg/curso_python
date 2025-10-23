agenda = {}

while True:
    print("\nOpciones:")
    print("1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Salir")
    opcion = input("Selecciona una opción (1, 2, 3): ")
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del contacto: ")
        telefono = input("Ingresa el número de teléfono: ")
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado.")
    elif opcion == "2":
    
        if agenda:
            print("\nContactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda está vacía.")
    elif opcion == "3":
        print("Saliendo de la agenda.")
        print(agenda)
        break
    else:
        print("Opción no válida. Intenta de nuevo.")