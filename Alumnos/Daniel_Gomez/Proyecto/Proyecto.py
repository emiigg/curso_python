import json
from pathlib import Path

DATA_FILE = Path("gastos.json")

def cargar_datos():
    """Carga los datos desde el archivo JSON. Si no existe, devuelve un diccionario vacío."""
    try:
        if DATA_FILE.exists():
            with DATA_FILE.open("r", encoding="utf-8") as f:
                return json.load(f)
        else:
            return {"categorias": {}}
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error al leer el archivo. Se iniciará con datos vacíos.")
        return {"categorias": {}}

def guardar_datos(datos):
    """Guarda los datos en el archivo JSON."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def crear_categoria(datos):
    """Permite al usuario crear una nueva categoría."""
    nombre = input("Nombre de la nueva categoría: ").strip().lower()
    if not nombre:
        print("Nombre inválido.")
        return
    if nombre in datos["categorias"]:
        print("La categoría ya existe.")
        return
    datos["categorias"][nombre] = []
    print(f"Categoría '{nombre}' creada exitosamente.")

def registrar_gasto(datos):
    """Registra un nuevo gasto en una categoría existente."""
    if not datos["categorias"]:
        print("No hay categorías disponibles. Crea una primero.")
        return

    print("Categorías disponibles:")
    for cat in datos["categorias"]:
        print(f" - {cat}")
    categoria = input("En qué categoría registras el gasto: ").strip().lower()

    if categoria not in datos["categorias"]:
        print("Categoría no encontrada.")
        return

    try:
        monto = float(input("Monto del gasto: "))
        if monto <= 0:
            print("El monto debe ser positivo.")
            return
    except ValueError:
        print("Monto inválido. Debe ser un número.")
        return

    fecha = input("Fecha del gasto (YYYY-MM-DD) [Enter para hoy]: ").strip()
    if not fecha:
        from datetime import date
        fecha = str(date.today())

    # Generar ID único para el gasto
    gastos_categoria = datos["categorias"][categoria]
    id_gasto = max([g["id"] for g in gastos_categoria], default=0) + 1

    nuevo_gasto = {"id": id_gasto, "fecha": fecha, "monto": monto}
    datos["categorias"][categoria].append(nuevo_gasto)
    print(f"Gasto de {monto} registrado en '{categoria}' con ID {id_gasto}.")

def ver_gastos(datos):
    """Muestra todos los gastos o filtra por categoría."""
    if not datos["categorias"]:
        print("No hay categorías ni gastos registrados.")
        return

    print("Categorías disponibles:")
    for cat in datos["categorias"]:
        print(f" - {cat}")
    categoria = input("¿Ver gastos de qué categoría? (Enter para ver todos): ").strip().lower()

    if categoria and categoria not in datos["categorias"]:
        print("Categoría no encontrada.")
        return

    print("\nGastos registrados:")
    print("-" * 60)
    total = 0
    if categoria:
        gastos = datos["categorias"][categoria]
        print(f"Gastos en '{categoria}':")
        for g in gastos:
            print(f"ID: {g['id']}, Fecha: {g['fecha']}, Monto: {g['monto']}")
            total += g['monto']
    else:
        for cat, gastos in datos["categorias"].items():
            print(f"Gastos en '{cat}':")
            for g in gastos:
                print(f"  ID: {g['id']}, Fecha: {g['fecha']}, Monto: {g['monto']}")
                total += g['monto']
            print()
    print("-" * 60)
    print(f"Total general: {total:.2f}\n")

def actualizar_gasto(datos):
    """Actualiza un gasto existente (monto o categoría)."""
    if not datos["categorias"]:
        print("No hay gastos registrados.")
        return

    ver_gastos(datos)

    try:
        id_gasto = int(input("ID del gasto a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    categoria_actual = None
    gasto = None
    for cat, lista in datos["categorias"].items():
        for g in lista:
            if g["id"] == id_gasto:
                gasto = g
                categoria_actual = cat
                break
        if gasto:
            break

    if not gasto:
        print("Gasto no encontrado.")
        return

    print(f"Gasto encontrado: Fecha: {gasto['fecha']}, Monto: {gasto['monto']}, Categoría: {categoria_actual}")

    nueva_fecha = input(f"Nueva fecha (actual: {gasto['fecha']}) [Enter para no cambiar]: ").strip()
    if nueva_fecha:
        gasto["fecha"] = nueva_fecha

    try:
        nuevo_monto = input(f"Nuevo monto (actual: {gasto['monto']}) [Enter para no cambiar]: ").strip()
        if nuevo_monto:
            nuevo_monto = float(nuevo_monto)
            if nuevo_monto <= 0:
                print("El monto debe ser positivo.")
                return
            gasto["monto"] = nuevo_monto
    except ValueError:
        print("Monto inválido.")
        return

    nueva_categoria = input(f"Nueva categoría (actual: {categoria_actual}) [Enter para no cambiar]: ").strip().lower()
    if nueva_categoria and nueva_categoria != categoria_actual:
        if nueva_categoria not in datos["categorias"]:
            print("La categoría no existe. Debes crearla primero.")
            return
        # Mover gasto a la nueva categoría
        datos["categorias"][categoria_actual].remove(gasto)
        datos["categorias"][nueva_categoria].append(gasto)

    print(f"Gasto con ID {id_gasto} actualizado correctamente.")

def eliminar_gasto(datos):
    """Elimina un gasto específico."""
    if not datos["categorias"]:
        print("No hay gastos registrados.")
        return

    ver_gastos(datos)

    try:
        id_gasto = int(input("ID del gasto a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    categoria_actual = None
    gasto = None
    for cat, lista in datos["categorias"].items():
        for g in lista:
            if g["id"] == id_gasto:
                gasto = g
                categoria_actual = cat
                break
        if gasto:
            break

    if not gasto:
        print("Gasto no encontrado.")
        return

    confirm = input(f"¿Eliminar gasto ID {id_gasto} de {categoria_actual}? (s/n): ").lower()
    if confirm == 's':
        datos["categorias"][categoria_actual].remove(gasto)
        print(f"Gasto con ID {id_gasto} eliminado.")
    else:
        print("Eliminación cancelada.")

def menu():
    print("\n--- Control de Gastos CRUD ---")
    print("1. Crear categoria")
    print("2. Registrar gasto")
    print("3. Ver gastos")
    print("4. Actualizar gasto")
    print("5. Eliminar gasto")
    print("6. Salir")

def main():
    datos = cargar_datos()

    while True:
        menu()
        try:
            opcion = int(input("Selecciona una opcion: "))
        except ValueError:
            print("Opción inválida. Ingresa un número.")
            continue

        if opcion == 1:
            crear_categoria(datos)
        elif opcion == 2:
            registrar_gasto(datos)
        elif opcion == 3:
            ver_gastos(datos)
        elif opcion == 4:
            actualizar_gasto(datos)
        elif opcion == 5:
            eliminar_gasto(datos)
        elif opcion == 6:
            guardar_datos(datos)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")


main()