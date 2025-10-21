import random

def eligir_dificultad():
    print("Elige un nivel de dificultad:")
    print("1. Fácil (números entre 1 y 10)")
    print("2. Medio (números entre 1 y 50)")
    print("3. Difícil (números entre 1 y 100)")
    
    while True:
        eleccion = input("Ingresa 1, 2 o 3: ")
        if eleccion == '1':
            return 10
        elif eleccion == '2':
            return 50
        elif eleccion == '3':
            return 100
        else:
            print("Elección inválida. Por favor, intenta de nuevo.")
            
def pista_distancia(objetivo, intento):
    diferencia = abs(objetivo - intento)
    if diferencia <= 2:
        return "¡Muy caliente!"
    elif diferencia <= 5:
        return "Caliente"
    elif diferencia <= 10:
        return "Tibio"
    elif diferencia <= 20:
        return "Frío"
    else:
        return "Muy frío"
    
def jugar():
    limite_superior = eligir_dificultad()
    numero_objetivo = random.randint(1, limite_superior)
    intentos = 0
    
    print(f"He elegido un número entre 1 y {limite_superior}. ¡Adivínalo!")
    
    while True:
        try:
            intento = int(input("Tu intento: "))
            intentos += 1
            
            if intento < 1 or intento > limite_superior:
                print(f"Por favor, ingresa un número entre 1 y {limite_superior}.")
                continue
            
            if intento == numero_objetivo:
                print(f"¡Felicidades! Has adivinado el número {numero_objetivo} en {intentos} intentos.")
                break
            else:
                pista = pista_distancia(numero_objetivo, intento)
                print(pista)
                
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
            
jugar()
print("-----------------------------------------------------------")