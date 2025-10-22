import random
import os
import sys

def limpiar_pantalla():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        pass  


def obtener_palabra():
    try:
        palabras = [
            "computadora", "avion", "chocolate", "ventana", "montaña", "reforestacion",
            "ingenieria", "pelicula", "biblioteca", "universidad", "gimnasio",
            "tigre", "familia", "musculo", "robot", "dron", "mazapan", "hablando",
            "carretera", "volcan", "playa", "camioneta", "bosque", "planeta", "cajeta"
        ]
        return random.choice(palabras).lower()
    except Exception as e:
        print("Error al obtener la palabra:", e)
        sys.exit(1)


def mostrar_progreso(palabra, letras_acertadas):
    try:
        return " ".join([letra if letra in letras_acertadas else "_" for letra in palabra])
    except Exception:
        return "_ " * len(palabra)


def juego_ahorcado():
    try:
        palabra = obtener_palabra()
        intentos_restantes = 6
        letras_acertadas = set()
        letras_intentadas = set()

        print("¡Bienvenido al juego del Ahorcado!")
        print(f"La palabra tiene {len(palabra)} letras.")

        while intentos_restantes > 0:
            try:
                print("\n" + mostrar_progreso(palabra, letras_acertadas))
                print(f"Intentos restantes: {intentos_restantes}")
                print(f"Letras usadas: {', '.join(sorted(letras_intentadas)) if letras_intentadas else 'Ninguna'}")

                intento = input("Adivina una letra: ").lower().strip()

                if not intento:
                    print("No ingresaste nada. Intenta de nuevo.")
                    continue

                if len(intento) != 1 or not intento.isalpha():
                    print("Ingresa solo una letra válida (sin números ni símbolos).")
                    continue

                if intento in letras_intentadas:
                    print("Ya intentaste esa letra. Prueba otra.")
                    continue

                letras_intentadas.add(intento)

                if intento in palabra:
                    letras_acertadas.add(intento)
                    print("¡Correcto!")
                else:
                    intentos_restantes -= 1
                    print("Letra incorrecta.")

                if all(letra in letras_acertadas for letra in palabra):
                    print("\n¡Felicidades! Adivinaste la palabra:", palabra.upper())
                    break

            except KeyboardInterrupt:
                print("\nJuego interrumpido por el usuario.")
                sys.exit(0)
            except Exception as e:
                print(f"Error inesperado: {e}")
                continue

        else:
            print("\nTe quedaste sin intentos. La palabra era:", palabra.upper())

    except Exception as e:
        print(f"Error crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        limpiar_pantalla()
        juego_ahorcado()
    except Exception as e:
        print(f"Error al iniciar el juego: {e}")
