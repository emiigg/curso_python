import random

OPCIONES = ("piedra", "papel", "tijera")

def gana(a, b):
    ganar = True
    
    if (a == "tijera" and b == "papel"):
        ganar = False
    elif (a == "papel" and b == "piedra"):
        ganar = False
    elif (a == "piedra" and b == "tijera"):
        ganar = False  
    elif (a == b):
        ganar = False
    
    return ganar

def jugar():
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    
    while True:
        
        try:
            eleccion_usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
            
            if eleccion_usuario == 'salir':
                print("Gracias por jugar. ¡Hasta luego!")
                break
            
            if eleccion_usuario not in OPCIONES:
                #print("Opción inválida. Por favor, elige piedra, papel o tijera.")
                raise ValueError("Opción inválida. Por favor, elige piedra, papel o tijera.")    
            
            eleccion_computadora = random.choice(OPCIONES)
            print(f"La computadora eligió: {eleccion_computadora}")
            
            if gana(eleccion_usuario, eleccion_computadora):
                print("¡Ganaste!")
            elif eleccion_usuario == eleccion_computadora:
                print("¡Empate!")
            else:
                print("¡Perdiste!")
        
        #except ValueError as ve:
         #   print("Valor incorrecto: ", ve)
        except Exception as e:
            print(type(e).__name__)
            print("Error desconocido: ", e)
        finally:
            print("-----------------------------------------------------------")
    
    
jugar()
    