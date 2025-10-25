import random

PALABRAS = (
    "sonic", "pokemon", "mario", "rubik", 
    "shadow", "pacman", "megaman", "python", "computadora"
)
VIDAS_INICIALES = 5

def jugar():
    print("¿Quieres jugar al ahorcado?")
    palabra_secreta = random.choice(PALABRAS)
    letras_adivinadas = []
    vidas = VIDAS_INICIALES
    juego_ganado = False
    
    while vidas > 0:
        if juego_ganado:
            break
            
        print(f"Te quedan {vidas} vidas.")
        progreso_actual = ""
        
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                progreso_actual += letra + " "
            else:
                progreso_actual += "_ "
        
        print(f"Palabra: {progreso_actual.strip()}")
        
        if letras_adivinadas:
            letras_ordenadas = letras_adivinadas[:]
            letras_ordenadas.sort()
            print(f"Letras usadas: {', '.join(letras_ordenadas)}")
        
        letra_usuario = input("Elige una letra: ").lower()
        letras_adivinadas.append(letra_usuario)
        
        if letra_usuario in palabra_secreta:
            print(f"La letra '{letra_usuario}' está en la palabra.")
            todas_adivinadas = True
            for letra in palabra_secreta:
                if letra not in letras_adivinadas:
                    todas_adivinadas = False
                    break
            
            if todas_adivinadas:
                juego_ganado = True
                
        else:
            print(f"La letra '{letra_usuario}' no está.")
            vidas -= 1
        
        print("-----------------------------------------------------------")
    
    if juego_ganado:
        print(f"\n¡Esoooo! Adivinaste la palabra: {palabra_secreta}")
    else:
        print(f"\n¡Game Over! La palabra era: {palabra_secreta}")

jugar()
