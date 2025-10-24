from pathlib import Path
import json

USERS_FILE = Path("Clase 6/users.json")

def cargar_usuarios():
    if not USERS_FILE.exists():
        return {}
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}

def iniciar_sesion():
    usuarios = cargar_usuarios()
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")


def registrarse():
    usuarios = cargar_usuarios()
    username = input("Elija un nombre de usuario: ")
    if username in usuarios:
        print("El nombre de usuario ya existe. Por favor, elija otro.")
        return
    password = input("Elija una contraseña: ")
    usuarios[username] = password
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(usuarios, file)
    print("Usuario registrado exitosamente.")


def menu():
    while True:
        print("--- Menú de Login ---")
        print("1. Iniciar sesión")
        print("2. Registrarse")
        print("3. Ver usuarios registrados")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ") 
        if opcion == "1":
            iniciar_sesion()  
        elif opcion == "2":
            registrarse()   
        elif opcion == "3":
            ver_usuarios()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")  