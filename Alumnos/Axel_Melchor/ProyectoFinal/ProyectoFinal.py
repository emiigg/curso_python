import random 

ARCHIVO_PUNTOS = "puntaje.txt"

def cargar_puntaje():
    """
    Carga los puntajes desde el archivo.
    """
    puntajes = {}
    with open(ARCHIVO_PUNTOS, "a+") as archivo:
       
        archivo.seek(0) 
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                usuario = partes[0]
                puntos = int(partes[1])
                puntajes[usuario] = puntos
    return puntajes

def guardar_puntaje(usuario, puntos_nuevos): 
    """
    Guarda el puntaje si es un récord personal.
    """
    puntos = cargar_puntaje()
    if usuario not in puntos or puntos_nuevos < puntos[usuario]:
        print(f"¡Nuevo récord para {usuario}: {puntos_nuevos} intentos!")
        puntos[usuario] = puntos_nuevos


        with open(ARCHIVO_PUNTOS, "w") as archivo:
            for u, p in puntos.items():
                archivo.write(f"{u},{p}\n")
    else:
        print(f"Tu puntaje fue {puntos_nuevos}. Tu récord personal sigue siendo {puntos[usuario]} intentos.")

def mostrar_puntajes():
    """
    Muestra los puntajes ordenados del mejor (menos intentos) al peor.
    """
    puntajes = cargar_puntaje()
    if not puntajes:
        print("\n--- No hay puntajes registrados. ---")
        return
    
    print("\n----- Puntajes Registrados (Menos intentos es mejor) -----")
    
    
    puntajes_ordenados = sorted(puntajes.items(), key=lambda item: item[1])
    
    for usuario, puntos in puntajes_ordenados:
        print(f"{usuario}: {puntos} intentos")
        
    print("---------------------------------------------------------")

def elegir_dificultad():
    """
    Pregunta al usuario la dificultad y devuelve el número máximo.
    """
    print("\nSeleccione la dificultad:")
    print("1. Fácil (números del 1 al 10)")
    print("2. Medio (números del 1 al 50)")
    print("3. Difícil (números del 1 al 100)")
    
    while True:
        eleccion = input("Ingrese 1, 2 o 3: ")
        if eleccion == "1":
            return 10
        elif eleccion == "2":
            return 50
        elif eleccion == "3":
            return 100
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

def pista_distancia(objetivo, intento):
    """
    Devuelve una pista de "frío" o "caliente" según la distancia.
    """
    diferencia = abs(objetivo - intento)
    if diferencia <= 2:
        return "¡Muy caliente!"
    elif diferencia <= 5:
        return "¡Caliente!"
    elif diferencia <= 10:
        return "Tibio."
    elif diferencia <= 20:
        return "Frío."
    else:
        return "¡Muy frío!"
    
def jugar_adivina_el_numero(usuario):
    """
    Función principal del juego.
    """
    limite_superior = elegir_dificultad()
    numero_objetivo = random.randint(1, limite_superior)
    intentos = 0
    adivinado = False 

    print(f"\nHe elegido un número entre 1 y {limite_superior}. ¡Intenta adivinarlo!")

    while not adivinado:
        try: 
            intentos_str = input("Ingrese su intento: ")
            intento = int(intentos_str)
            intentos += 1

            if intento < 1 or intento > limite_superior:
                print(f"Por favor, ingrese un número entre 1 y {limite_superior}.")
                continue

            if intento == numero_objetivo:
                adivinado = True
                print(f"¡Felicidades, {usuario}! ¡Has adivinado el número en {intentos} intentos!")
            else:
                pista = pista_distancia(numero_objetivo, intento)
                print(pista)

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")

    
    guardar_puntaje(usuario, intentos)

def menu_principal():
    """
    Maneja el menú principal y el flujo del programa.
    """
    print("----- Bienvenido al Juego de Adivina el Número -----")
    usuario = input("Por favor, ingrese su nombre de usuario: ")

    while True:
        print(f"\n--- Usuario Actual: {usuario} ---")
        print("Elija una opción:")
        print("1. Jugar Adivina el Número")
        print("2. Ver Puntajes")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")
        if opcion == "1":
            jugar_adivina_el_numero(usuario)
        elif opcion == "2":
            mostrar_puntajes()
        elif opcion == "3":
            print(f"Gracias por jugar, {usuario}. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()