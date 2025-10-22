def ahorcado():
    print("Bienvenido al juego del Ahorcado")
    print("--------------------------------------------------------")
    
    # Jugador 1 ingresa la palabra secreta
    palabra_secreta = input("Jugador 1: Escribe una palabra para adivinar ").lower()
    # Limpieza de pantalla (solo estético, se puede comentar si quieres)
    print("\n" * 10)
    print("Palabra guardada con exito\n")
    
    # Convertimos la palabra en una lista de caracteres
    palabra_lista = list(palabra_secreta)
    
    # Inicializamos la palabra a adivinar con guiones bajos
    palabra_adivinada = ["_" for _ in palabra_lista]
    
    intentos = 6  # Inteentos (Es un intento por cada parte del monito,cabeza,cuerpo,brazo izquierdo,brazo derecho,pierna izquierda y pierna derecha)
    letras_usadas = set()
    
    while intentos > 0: #Bucle que se repite siempre y cuando el usuario aun tenga intentos
        print("Palabra: " + " ".join(palabra_adivinada))
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {', '.join(letras_usadas) if letras_usadas else 'Ninguna'}")
        
        letra = input("Jugador 2, elige una letra: ").lower()
        
        # Validación de entrada (Esto permite basicamente que el usuario solo ingrese una letra y no numeros o simbolos)
        if len(letra) != 1 or not letra.isalpha():
            print("ERROR: Elije una letra a-z.\n")
            continue
        
        if letra in letras_usadas: #Si la letra ya se uso,va a pedir al usuario que ingrese otra letra
            print("Esta letra ya se uso, intenta con otra.\n")
            continue
        
        letras_usadas.add(letra) #Se agrega la letra a las letras usadas 
        
        # Comprobamos si la letra está en la palabra
        if letra in palabra_lista:
            print("La letra si esta en la palabra.\n")
            for i in range(len(palabra_lista)):#Aqui basicamente se comparan ambas listas, si lista a==lista b en el espacio i
                if palabra_lista[i] == letra:
                    palabra_adivinada[i] = letra
        else:
            intentos -= 1
            print("Esa letra no está en la palabra.\n")
        
        # Comprobamos si ya se adivinó la palabra
        if palabra_adivinada == palabra_lista:
            print("Haz ganadoooo: Toma una picafresa :D")
            print(f"La palabra era: {palabra_secreta}")
            break
    else:
        print("Haz perdido :ccc")
        print(f"La palabra correcta era: {palabra_secreta}")
# LLamamo a la funcion para que se ejecute el codigo
ahorcado()
