import random

PALABRAS = (
    "carro", "helicoptero", "computadora", "avion", 
    "desarrollo", "codigo", "mama", "java", "variable"
)
VIDAS_INICIALES = 6


def obtener_palabra(lista_palabras):
    """Elige una palabra aleatoria de la lista."""
    return random.choice(lista_palabras)

def mostrar_progreso(palabra, letras_adivinadas):

    progreso = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

def verificar_victoria(palabra, letras_adivinadas):
    for letra in palabra:
        if letra not in letras_adivinadas:
            return False 
    return True 



def jugar():
    print("Bienvenido al Juego del Ahorcado")
    
    palabra_secreta = obtener_palabra(PALABRAS)
    letras_adivinadas = set()
    vidas = VIDAS_INICIALES
    juego_ganado = False
    
    while vidas > 0 and not juego_ganado:
        
        print(f"\nTe quedan {vidas} vidas.")
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(f"Palabra: {progreso_actual}")
        
        if letras_adivinadas:
            print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}")
        
        try:
            letra_usuario = input("Elige una letra: ").lower()
            
            if len(letra_usuario) != 1 or not letra_usuario.isalpha():
                raise ValueError("Entrada inválida. Debes ingresar solo una letra.")
            
            if letra_usuario in letras_adivinadas:
                raise ValueError(f"Ya intentaste con la letra '{letra_usuario}'.")
            
            letras_adivinadas.add(letra_usuario)
            
            if letra_usuario in palabra_secreta:
                print(f"¡Bien! La letra '{letra_usuario}' está en la palabra.")
                
                if verificar_victoria(palabra_secreta, letras_adivinadas):
                    juego_ganado = True
                    
            else:
                print(f"¡Incorrecto! La letra '{letra_usuario}' no está.")
                vidas -= 1
        
        
        except ValueError as ve:
            print(type(ve).__name__)
            print("Error: ", ve)
            
        
        except Exception as e:
            print(type(e).__name__)
            print("Error desconocido: ", e)
            
        
        finally:
            print("-----------------------------------------------------------")

    
    
    if juego_ganado:
        print(f"Adivinaste la palabra: {palabra_secreta}")
    else:
        print("Te quedaste sin vidas.")
        print(f"La palabra secreta era: {palabra_secreta}")


jugar()
