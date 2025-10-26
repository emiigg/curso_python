import random

def dificultad():
    print("Elige un nivel de dificultad: ")
    print("1. Facil (numeros entre 1 y 10)")
    print("2. Facil (numeros entre 1 y 50)")
    print("3. Facil (numeros entre 1 y 100)")

    while True:
        eleccion = input("Ingresa 1, 2 o 3: ")
        if eleccion == "1": 
            return 10
        elif eleccion == "2":
            return 50
        elif eleccion == "3":
            return 100
        else:
            print("Elcción inválida. Ingrese un valor válido.")

def pista_distancia(objetivo, intento):
    diferencia = abs(objetivo - intento)
    if diferencia <= 2:
        return "Muy caliente"
    elif diferencia <= 5:
        return "Caliente"
    elif diferencia <= 10:
        return "tibio"
    elif diferencia <= 20:
        return "frio"
    else:
        "muy frio"

def jugar():
    limite_superior = dificultad()
    numero_objetivo = random.randint(1, limite_superior)
    intentos = 0

    print(f"Se ha elegido un valor entre 1 y {limite_superior}. Adivinale")

    while True:
        intento = int(input("Ingresa tu inento: "))
        intentos += 1

        if intento < 1 or intento > limite_superior:
            print(f"Por favor ingresa un valor entre 1 y {limite_superior}")
            continue
        if intento == numero_objetivo:
            print(f"Felicidades,. Adivinaste el número {numero_objetivo} en {intentos} intentos.")
            break
        else:
            pista = pista_distancia(numero_objetivo, intento)
            print(pista)

jugar()