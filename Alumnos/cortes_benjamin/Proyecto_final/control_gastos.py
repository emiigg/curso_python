from pathlib import Path

print("-------CONTROL DE GASTOS-------")

# Archivo donde se guardarán los gastos de la forma que habiamos visto no pude y busque otra forma. 
ruta_carpeta_script = Path(__file__).parent
ruta = ruta_carpeta_script / "gastos.txt"


gastos = {}

def registrar_gasto():
    try:
        categoria = input("Ingrese la categoría del gasto (por ejemplo: comida, transporte, ocio): ").capitalize()
        monto = float(input("Ingrese el monto del gasto: "))
        
        if categoria in gastos:
            gastos[categoria] += monto
        else:
            gastos[categoria] = monto

        # Guardar en el archivo
        with ruta.open("a", encoding="utf-8") as archivo:
            archivo.write(f"{categoria},{monto}\n")

        print(f"Gasto registrado correctamente: {categoria} -> ${monto}")
    except ValueError:
        print("Error: el monto debe ser un número.")
    except Exception as e:
        print(f"Ocurrió un error al registrar el gasto: {e}")


def cargar_gastos():
    if not ruta.exists():
        print("No hay registros previos. Se creará un nuevo archivo de gastos.")
        ruta.touch()
        return

    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip():
                    categoria, monto = linea.strip().split(",")
                    monto = float(monto)
                    if categoria in gastos:
                        gastos[categoria] += monto
                    else:
                        gastos[categoria] = monto
    except Exception as e:
        print(f"Error al cargar los gastos: {e}")


def mostrar_resumen():
    if not gastos:
        print("No hay gastos registrados aún.")
        return

    print("\n-------RESUMEN DE GASTOS-------")
    total = 0
    for categoria, monto in gastos.items():
        print(f"{categoria}: ${monto:.2f}")
        total += monto
    print(f"\nTotal general: ${total:.2f}")
    print("-------------------------------")


def menu():
    """Menú principal del programa"""
    cargar_gastos()
    
    while True:
        print("""
------- MENÚ PRINCIPAL -------
1. Registrar gasto
2. Ver resumen por categoría
3. Salir
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_resumen()
        elif opcion == "3":
            print("¡Hasta luego! Tus gastos se han guardado correctamente.")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    menu()
