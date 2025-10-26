from pathlib import Path
import json

FILE = Path("proyecto final/categorias.json") #es el archivo con todas las categorias en formato .json

def categorias():
    if not FILE.exists():
        return {}
    try:
        with FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("Error al leer el archivo.")
        return {}

def main_menu(): #este es el menu principal del controlador, el usuario selecciona cual de las 3 opciones quiere realizar
    categoria = categorias()

    while True:
        print("Bienvenido a su controlador de gastos.\n¿Qué desea hacer hoy?")
        print("1. Agregar nuevo gasto.")
        print("2. Ver gastos.")
        print("3. salir.")

        opcion = input("Seleccione una de las opciones anteriores:\n")
        if opcion == "1":
            print("Has seleccionado: Agregar nuevo gasto.")
            OP1(categoria)
            
        elif opcion == "2":
            print("Has seleccionado: Ver gastos.")
            OP2(categoria)

        elif opcion == "3":
            print("Has salido del programa.")
            break
        else:
            print("Opcion inválida")

def guardar_categorias(data):
    try:
        with FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        print("\nCambio guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar el cambio: {e}")

def sumar_gastos(categoria): #suma todos los gastos de todas las categorias
    total = 0
    for nombre_categoria, datos_gasto in categoria.items():
        total += datos_gasto.get("cantidad", 0)
    return total

def OP1(categoria): # esta funcion sirve para mostrar el menu de agregar nuevo gasto
    print("\nSelecciona la categoría de gasto: ")
    print("1. Comida")
    print("2. Transporte")
    print("3. Golosinas")
    print("4. Tarjetas de credito (TDC)")
    print("5. Salir")

    opciones_gasto = { #diccionario para simplificar los if
        1: "comida", 
        2: "transporte", 
        3: "golosinas", 
        4: "TDC"
    }

    try: #este try (segun yo) es por si se introduce algun caracter especial como opcion
        while True:
            eleccion = input("Escribe tu eleccion: 1, 2, 3, 4, 5\n ")

            if eleccion == "5":
                print("Regresando al menu principal\n")
                break

            if eleccion.isdigit() and int(eleccion) in opciones_gasto:
                eleccion_int = int(eleccion)
                clave = opciones_gasto[eleccion_int]
                
                print(f"Has seleccionado la categoria: {clave}")
                
                try:
                    gasto = float(input("\nIngresa cuanto gastaste en esa transaccion: "))
                    if gasto <= 0:
                        print(f"Ingrese un valor correcto no {gasto}")
                        continue

                    datos_gasto = categoria.setdefault(clave, {"cantidad": 0}) #si no existe cantidad dentro de la categoria, la crea y la deja en cero
                    
                    datos_gasto["cantidad"] = datos_gasto.get("cantidad", 0) + gasto #suma el nuevo gasto al anterior

                    guardar_categorias(categoria)
                    
                except ValueError:
                    print("Error: El gasto debe ser un número valido.")
            else:
                print("Opcion invalida")
    
    except Exception as a: 
        print(f"Ocurrio un error: {a}")



def OP2(categoria): #funcion del menu de cual categoria de gastos se quiere visualizar
    

    claves_mapeadas = {
        1: "comida",
        2: "transporte",
        3: "golosinas",
        4: "TDC",
    }

    try:

        while True:
            print("\nSelecciona la categoria de gastos que quieres ver: ")
            print("1. Comida")
            print("2. Transporte")
            print("3. Golosinas")
            print("4. Tarjetas de credito (TDC)")
            print("5. Total")
            print("6. Salir")


            eleccion = input("Escribe tu elección (1-6): ")

            if eleccion.isdigit():
                eleccion = int(eleccion)

                if eleccion == 6:
                    print("Regresando al menu principal.\n")
                    break # Sale de OP2 y regresa al loop de main_menu
            
                elif eleccion == 5:
                    # Suma total de todos los gastos
                    total = sumar_gastos(categoria)
                    print(f"El gasto total general es:\n{total}\n")

                elif eleccion in claves_mapeadas:
                    clave_a_buscar = claves_mapeadas[eleccion]
                
                    # Accede al diccionario interno de la categoría
                    gasto_categoria = categoria.get(clave_a_buscar)

                    if gasto_categoria:
                        # Suma el valor especifico de cantidad
                        monto = gasto_categoria.get("cantidad", 0)
                        print(f"\nEl total de gastos en {clave_a_buscar} es: {monto}\n")
                    else:
                        print(f"Aún no hay gastos registrados para la categoría {clave_a_buscar}.")
            
                else:
                    print("Opción inválida. Intente de nuevo.")
            else:
                print("Entrada inválida. Por favor, ingresa un número.")
    
    except Exception as e:
        print(f"Erros al seleccioar una opcion: {e}")


main_menu()