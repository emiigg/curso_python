import random

# === Adivina el número (Frío o Caliente) ===
puntajes = {}

def jugar(usuario):
    print("\n¡Bienvenido al juego, " + usuario + "!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            intento = int(input("Adivina el número (1-100): "))
            intentos += 1

            if intento == numero_secreto:
                print(f"¡Felicidades, {usuario}! Adivinaste el número en {intentos} intentos.")
                puntaje = 100 - (intentos - 1) * 10
                puntaje = max(puntaje, 10)  # el mínimo puntaje será 10
                print(f"Tu puntaje: {puntaje}")
                # Guardar puntaje más alto
                if usuario not in puntajes or puntaje > puntajes[usuario]:
                    puntajes[usuario] = puntaje
                    print("Nuevo puntaje más alto registrado.")
                else:
                    print(f"Tu puntaje más alto sigue siendo: {puntajes[usuario]}")
                break

            elif abs(intento - numero_secreto) <= 5:
                print("¡Caliente!")
            elif abs(intento - numero_secreto) <= 10:
                print("Tibio...")
            else:
                print("Frío.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Jugar 'Adivina el número'")
    print("2. Mostrar puntajes")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        usuario = input("\nIngresa tu nombre de usuario: ")
        jugar(usuario)

    elif opcion == "2":
        print("\n === PUNTAJES ===")
        if not puntajes:
            print("Aún no hay puntajes registrados.")
        else:
            for jugador, puntaje in puntajes.items():
                print(f"{jugador}: {puntaje}")

    elif opcion == "3":
        print("\nGracias por jugar. ¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Intenta de nuevo.")
