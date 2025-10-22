import random

palabras = ['python', 'java', 'kotlin', 'javascript', 'humano', 'programacion', 'desarrollo', 'computadora', 'teclado', 'monitor']

def elegir_palabra():
    return random.choice(palabras)
def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + ' '
        else:
            tablero += '_ '
    return tablero.strip()
def jugar_ahorcado():
    palabra_secreta = elegir_palabra()
    letras_adivinadas = set()
    intentos_restantes = 6

    print("¡Bienvenido al juego del Ahorcado!")
    
    while intentos_restantes > 0:
        try:
            print("\n" + mostrar_tablero(palabra_secreta, letras_adivinadas))
            print(f"Intentos restantes: {intentos_restantes}")
            letra = input("Adivina una letra: ").lower()

            if len(letra) != 1 or not letra.isalpha():
                print("Por favor, ingresa una sola letra válida.")
                continue

            if letra in letras_adivinadas:
                print("Ya has adivinado esa letra. Intenta con otra.")
                continue

            letras_adivinadas.add(letra)

            if letra not in palabra_secreta:
                intentos_restantes -= 1
                print(f"La letra '{letra}' no está en la palabra.")

            if all(letra in letras_adivinadas for letra in palabra_secreta):
                print("\n¡Felicidades! Has adivinado la palabra:", palabra_secreta)
                break
        except Exception as e:
            print("Ha ocurrido un error:", e)
    else:
            print("\nHas perdido. La palabra era:", palabra_secreta)
            print("Ejecucion finalizada")


jugar_ahorcado()