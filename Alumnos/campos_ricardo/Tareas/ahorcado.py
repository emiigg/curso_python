import random

# === JUEGO DEL AHORCADO ===

palabras = ["python", "programacion", "computadora", "internet", "teclado", "pantalla", "juego", "ahorcado"]

def jugar_ahorcado():
    palabra = random.choice(palabras)
    letras_adivinadas = []
    intentos_restantes = 6
    gano = False

    print("\n🎮 ¡Bienvenido al juego del Ahorcado!")
    print("Adivina la palabra letra por letra.")
    print(f"Tienes {intentos_restantes} intentos.\n")

    while intentos_restantes > 0 and not gano:
        # Mostrar progreso
        progreso = ""
        for letra in palabra:
            if letra in letras_adivinadas:
                progreso += letra + " "
            else:
                progreso += "_ "
        print("Palabra:", progreso.strip())

        # Verificar si ya ganó
        if all(letra in letras_adivinadas for letra in palabra):
            gano = True
            break

        # Pedir letra
        letra_usuario = input("Ingresa una letra: ").lower()

        # Validaciones
        if not letra_usuario.isalpha() or len(letra_usuario) != 1:
            print("⚠️ Por favor, ingresa solo una letra.\n")
            continue

        if letra_usuario in letras_adivinadas:
            print("Ya habías ingresado esa letra. Intenta con otra.\n")
            continue

        # Verificar si la letra está en la palabra
        letras_adivinadas.append(letra_usuario)
        if letra_usuario in palabra:
            print("✅ ¡Bien! La letra está en la palabra.\n")
        else:
            intentos_restantes -= 1
            print(f"❌ Esa letra no está. Te quedan {intentos_restantes} intentos.\n")

    # Resultado final
    if gano:
        print(f"🎉 ¡Felicidades! Adivinaste la palabra '{palabra}'.")
    else:
        print(f"💀 Te quedaste sin intentos. La palabra era '{palabra}'.")
    print("Fin del juego.\n")


# === MENÚ PRINCIPAL ===
while True:
    print("=== MENÚ DEL AHORCADO ===")
    print("1. Jugar")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        jugar_ahorcado()
    elif opcion == "2":
        print("\nGracias por jugar. ¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.\n")
