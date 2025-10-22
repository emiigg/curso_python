import random

palabras = ["Tarea", "programa", "computadora", "calculo", "python", "juego"]

palabra = random.choice(palabras)
letras_adivinadas = []
intentos = 6 

print("¡Bienvenido al juego del Ahorcado!")
print("Adivina la palabra ")


while intentos > 0:
    palabra_mostrada = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + " "
        else:
            palabra_mostrada += " _ "
    print("\n" + palabra_mostrada)

    if "_" not in palabra_mostrada:
        print("Felicidades! Adivinaste la palabra")
        break


    letra = input("Ingresa una letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Ingrese solo una letra (NO signos ni números)")
        continue
        

    if letra in letras_adivinadas:
        print("Ya usaste esa letra.")
        continue

    letras_adivinadas.append(letra)


    if letra not in palabra:
        intentos -= 1
        print(f"Letra incorrecta. Te quedan {intentos} intentos.")
    else:
        print("Bien")


if intentos == 0:
    print("\n Perdiste! La palabra era:", palabra)