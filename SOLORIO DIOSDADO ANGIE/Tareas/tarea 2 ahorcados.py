import random

def jugar_ahorcado():
    palabra = random.choice(["python", "programacion", "desarrollo", "inteligencia", "supercalifragilisticoespialidoso", "gato", "tiktok", "patos"])
    #random.choice selecciona un elemento aleatorio de una lista o tupla
    #[] sirve para definir listas
    print("¡Bienvenido al juego del ahorcado!")
    print("La palabra tiene", len(palabra), "letras.") #len sirve para contar caracteres
    letras_elegidas = [] #sirve para almacenar las letras que el usuario ha adivinado
    intentos = 6 #intentos permitidos
  
    while intentos > 0:
        try: #manejo de excepciones
            letra = input("Adivina una letra: ")
            if len(letra) != 1 or not letra.isalpha():
                raise ValueError("Por favor, ingresa una sola letra válida.")
        except ValueError as e: #captura errores específicos
            print("Error de valor:", e)
            continue #continua con la siguiente iteración del bucle
        if letra in  letras_elegidas:
            print("Ya adivinaste esa letra.")
        elif letra in palabra:
            print("¡Correcto!")
            letras_elegidas.append(letra)
        else:
            print("Incorrecto.")
            letras_elegidas.append(letra) #.append sirve para agregar elementos a una lista, llevar el conteo de las letras que el usuario ha adivinado
            intentos -= 1 #resta un intento por cada letra incorrecta
        print("Letras elegidas:", letras_elegidas)
        palabra_oculta = "".join([letra if letra in letras_elegidas else "_" for letra in palabra]) #join sirve para unir elementos de una lista en una cadena
        # el codigo dentro de [] es una lista por comprensión que crea una nueva lista con las letras adivinadas y guiones bajos para las letras no adivinadas
        print("Palabra:", palabra_oculta)
        if "_" not in palabra_oculta: #not in sirve para verificar si un elemento no está presente en una secuencia 
            print("¡Ganaste!")
            break
        
    else:
        print("Perdiste. La palabra era:", palabra)
        print("Gracias por jugar. ¡Hasta la próxima!")
    
jugar_ahorcado()    
print("-----------------------------------------------------------")    