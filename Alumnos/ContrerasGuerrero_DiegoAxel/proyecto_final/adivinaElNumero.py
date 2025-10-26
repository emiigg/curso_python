from pathlib import Path
import json
import random

ARCHIVO_PUNTAJES = Path("Alumnos/ContrerasGuerrero_DiegoAxel/proyecto_final/puntajes.json")

def cargar_puntajes():
    if ARCHIVO_PUNTAJES.exists():
        try:
            with open(ARCHIVO_PUNTAJES, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error al leer los puntajes. Se reiniciará el archivo.")
    return {}

def guardar_puntajes(puntajes):
    with open(ARCHIVO_PUNTAJES, "w", encoding="utf-8") as f:
        json.dump(puntajes, f, indent=4, ensure_ascii=False) #agregué este parametro para que acepte caracteres especiales

def mostrar_puntajes(puntajes):
    rango = 1
    if not puntajes:
        print("No hay puntajes registrados aún.")
        return
    print("\n==PUNTAJES GUARDADOS==")
    for jugador, puntaje in sorted(puntajes.items(), key=lambda x: x[1]): #metodo de ordenamiento investigado
        print(f" {rango}. {jugador}: {puntaje} intentos")
        rango += 1

def eleccion_de_limite_superior():
    while True:
        try:
            eleccion = int(input("Elige el numero limite del rango (mínimo 50): "))
            if eleccion >= 50:
                return eleccion
            else:
                print("Debe ser al menos 50.")
        except ValueError:
            print("Entrada inválida. Ingresa un numero entero.")

def pista_de_distancia(objetivo, intento):
    diferencia = abs(objetivo - intento)
    pistas = [
        (2, "¡Muy caliente!"),
        (5, "Caliente"),
        (10, "Tibio"),
        (20, "Frio"),
        (float('inf'), "Muy frío")
    ]
    for limite, mensaje in pistas:
        if diferencia <= limite:
            return mensaje

def jugar(puntajes):
    usuario = input("\nIngresa tu nombre de usuario: ").strip() #metodo de string investigado tmb
    if not usuario:
        print("Nombre de usuario no puede estar vacio.")
        return

    limite_superior = eleccion_de_limite_superior()
    numero_objetivo = random.randint(1, limite_superior)
    intentos = 0

    print(f"\nSe ha elegido un numero entre 1 y {limite_superior}. ¡Adivnalo!")

    while True:
        try:
            intento = int(input("Tu intento: "))
            intentos += 1

            if intento < 1 or intento > limite_superior:
                print(f"Por favor, ingresa un numero entre 1 y {limite_superior}.")
                continue

            if intento == numero_objetivo:
                print(f"¡Felicidades {usuario}! Adivinaste el numero {numero_objetivo} en {intentos} intentos.")
                break
            else:
                print(pista_de_distancia(numero_objetivo, intento))

        except ValueError:
            print("Entrada inválida. Ingresa un numero entero.")

    # registro del puntaje
    mejor_puntaje = puntajes.get(usuario) #Igual, metodo de obtencion de usuario investigado
    if mejor_puntaje is None or intentos < mejor_puntaje:
        puntajes[usuario] = intentos
        print(f"Nuevo récord personal para {usuario} con {intentos} intentos!")
        guardar_puntajes(puntajes)
    else:
        print(f"Tu mejor puntaje sigue siendo {mejor_puntaje} intentos.")

def menu():
    puntajes = cargar_puntajes()

    while True:
        print("\n===== JUEGO CALIENTE Y FRIO =====")
        print("1. Jugar")
        print("2. Ver puntajes")
        print("3. Salir")

        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            jugar(puntajes)
        elif opcion == "2":
            mostrar_puntajes(puntajes)
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta pronto.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__": #sin esto no me ejecutaria, porque aqui defino el metodo principal
    menu()
