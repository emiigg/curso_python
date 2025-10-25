from pathlib import Path
import json

USERS_FILE = Path("Clase 6/users.json")


def cargar_usuarios():
    if not USERS_FILE.exists():
        return {}
    try:
        with USERS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("Error al leer el archivo de usuarios. El archivo puede estar corrupto.")
        return {}
            
def registrarse(users, contador):
    user = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    
    if user in users:
        print("El nombre de usuario ya existe. Intente con otro.")
        return
    
    users[user] = {"password": password}
    
    with USERS_FILE.open("w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)
        
    print("Usuario registrado exitosamente.")
    
def listar_usuarios(users):
    if not users:
        print("No hay usuarios registrados.")
        return
    print("Usuarios registrados:")
    for user in users:
        print(f"- {user}")
        
        
def iniciar_sesion(users):
    user = input("Ingrese su nombre de usuario: ")
    
    if user not in users:
        print("El usuario no existe.")
        return
    
    password = input("Ingrese su contraseña: ")
    if users[user]["password"] == password:
        print("Inicio de sesión exitoso.")
    else:
        print("Contraseña incorrecta.")



def menu():
    contador = 0
    print(contador)
    users = cargar_usuarios()
    while True:
        print("--- Menú de Login ---")
        print("1) Iniciar sesion")
        print("2) Registrarse")
        print("3) Listar usuarios")
        print("4) Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            iniciar_sesion(users)
        elif opcion == "2":
            registrarse(users, contador)
        elif opcion == "3":
            listar_usuarios(users)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()