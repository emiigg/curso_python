import random

listaPalabras = ["paralelepipedo","paralelogramo","electrocardiograma","encefalografia",
                "parangaricutirimicuaro","lapiz","folio","celular","laptop","mouse"]

def jugar():
    intentos = 6 
    gano = False
    print("=== JUEGO DEL AHORCADO ===")
    
    palabraSeleccionado = random.choice(listaPalabras)
    listaDeLetras = ["_"] * len(palabraSeleccionado)
    
    print(f"La palabra tiene: {len(palabraSeleccionado)} letras.\n")
    
    while intentos > 0:
        print("Palabra:", " ".join(listaDeLetras))
        print(f"Intentos: {intentos}")
        
        try: 
            letraActual = input("Ingrese una letra: ").lower()
        
            if len(letraActual) != 1 or letraActual not in "abcdefghijklmnopqrstuvwxyz":
                print("Ingresa solo una letra válida.")
                continue

        except ValueError as e:
            print("Error:", e)
            continue
        except Exception as e:
            print("Ocurrió un error inesperado:", e, "\n")
            continue
        
        if letraActual in palabraSeleccionado:
            for i in range(len(palabraSeleccionado)):
                if palabraSeleccionado[i] == letraActual:
                    listaDeLetras[i] = letraActual
            print("Correcto, letra encontrada\n")
        else:
            intentos -= 1
            print("Letra incorrecta\n")
            
        if "_" not in listaDeLetras:
            gano = True
            break
    
    if gano:
        print("Felicidades, has adivinado la palabra:", palabraSeleccionado)
    else:
        print("Te quedaste sin intentos. La palabra era:", palabraSeleccionado)
            
jugar()
print("================================")
