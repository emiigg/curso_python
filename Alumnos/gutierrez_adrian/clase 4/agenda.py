agenda = {}

while True:
    print("\nOpciones")
    print("1. Agregar contacto")
    print("2. Ver contacto")
    print("3. Salir")
    opcion = input("selecciona una opción (1, 2, 3): ")

    if opcion == "1":
        nombre = input("ingresa el nombre del contacto: ")
        telefono = input("ingresa el numero de telefono: ")
        agenda[nombre] = telefono
        print(f"contacto {nombre} agregado.")
    elif opcion == "2":
        if agenda:
            print("\ncontactos en la agenda:")
            for nombre, telefono in agenda.items():
                print(f"{nombre}: {telefono}")
        else:
            print("La agenda esta vacia.")
    elif opcion == 3:
        print("saliendo de la agenda.")
        print(agenda)
        break
    else:
        print("opcion no valida. intenta de nuevo.")   