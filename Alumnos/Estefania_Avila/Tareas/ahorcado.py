import random

# Diccionario de palabras por categoría
palabras = {
    "animal": ["perro", "gato", "elefante", "leon", "tigre"],
    "fruta": ["manzana", "banana", "naranja", "platano", "kiwi"],
    "ciudad": ["mexico", "paris", "londres", "berlin", "tokio"],
    "color": ["rojo", "azul", "verde", "amarillo", "negro"]
}

def es_letra(letra):
    return letra.isalpha()  # Más simple: True si es letra, False si no

def imprimir_palabra(lista):
    print(" ".join(lista))  # Imprime la palabra con espacios

def juego_de_ahorcados():
    categoria = random.choice(list(palabras.keys()))
    palabra = random.choice(palabras[categoria])

    palabra_oculta = ["_"] * len(palabra)
    letras_intentadas = []
    intentos = 6

    print("¡Bienvenido al juego de ahorcados! La categoría es:", categoria)

    while intentos > 0:
        imprimir_palabra(palabra_oculta)

        if "_" not in palabra_oculta:
            print("¡Felicidades! Has ganado. La palabra era:", palabra)
            return

        while True:
            letra = input("Ingrese una letra: ").lower()
            if letra in letras_intentadas:
                print("Ya has intentado esta letra. ¡Prueba con otra!")
            elif len(letra) != 1 or not es_letra(letra):
                print("Eso no es una letra. Ingrese solo una letra.")
            else:
                break

        letras_intentadas.append(letra)
        acierto = False

        for i, l in enumerate(palabra):
            if l == letra:
                palabra_oculta[i] = letra
                acierto = True

        if acierto:
            print("¡Acertaste!")
        else:
            intentos -= 1
            print("No forma parte de la palabra. Te quedan", intentos, "intentos.")

    print("¡Oh no! Has perdido. La palabra era:", palabra)

# Ejecutar el juego
juego_de_ahorcados()
