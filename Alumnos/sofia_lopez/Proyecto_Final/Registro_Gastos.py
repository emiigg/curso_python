# -----------------------------------------------
# Planeacion para el proyecto final de registro de gasto
# Planeacion de presupuesto semanal
# Categorias para los gastos:
# Registro diario y semanal
# -----------------------------------------------

# Inicio del programa
print("Bienvenid@ al sistema de registro de gastos")
nombre = str(input("Por favor ingresa tu nombre: "))
print(nombre + ", ¿Qué deseas hacer hoy?")
print("[1] Planeacion de presupuesto semanal")
print("[2] Registrar gastos")
print("[3] Ver resumen semanal")

opcion = int(input("Selecciona una opcion (1, 2 o 3): "))

# Diccionario para categorías
categorias = {
    "comida": 0.0,
    "transporte": 0.0,
    "entretenimiento": 0.0,
    "otros": 0.0
}

# Archivo donde se guardarán los registros
archivo = "registro_gastos.txt"

# Opción 1: Planeación de presupuesto semanal
if opcion == 1:
    presupuesto = float(input("Ingresa tu presupuesto semanal total: "))
    print("Tu presupuesto semanal es de:", presupuesto)

    print("--------Categorias de gastos-----")
    print("1 [comida]\n2 [transporte]\n3 [entretenimiento]\n4 [otros]\n5 [Salir]")

    presupuesto_categorias = {}
    while True:
        opcion_categoria = int(input("Selecciona una categoria para asignar presupuesto (1-5): "))
        if opcion_categoria == 5:
            break
        elif opcion_categoria in [1, 2, 3, 4]:
            nombre_categoria = ["comida", "transporte", "entretenimiento", "otros"][opcion_categoria - 1]
            monto = float(input(f"Ingrese el presupuesto asignado para {nombre_categoria}: "))
            presupuesto_categorias[nombre_categoria] = monto
        else:
            print("Opción no válida. Intenta de nuevo.")

    print("\nResumen del presupuesto semanal:")
    for cat, monto in presupuesto_categorias.items():
        print(f" - {cat.capitalize()}: ${monto:.2f}")

    # Guardar presupuesto en archivo
    with open(archivo, "a") as f:
        f.write(f"\n--- Presupuesto semanal de {nombre} ---\n")
        for cat, monto in presupuesto_categorias.items():
            f.write(f"{cat}: ${monto:.2f}\n")
        f.write(f"Presupuesto total: ${presupuesto:.2f}\n")

    print("\nPresupuesto guardado correctamente.")

# Opción 2: Registrar gastos
elif opcion == 2:
    print("\nRegistro de gastos")
    continuar = "si"

    while continuar.lower() == "si":
        gasto = float(input("Ingresa el monto del gasto: "))
        categoria = input("Ingresa la categoría del gasto (comida, transporte, entretenimiento, otros): ").lower()

        if categoria in categorias:
            categorias[categoria] += gasto
            print("Has registrado un gasto de", gasto, "en la categoría de", categoria)

            # Guardar el gasto en archivo
            with open(archivo, "a") as f:
                f.write(f"Gasto registrado: ${gasto:.2f} en {categoria}\n")

        else:
            print("Categoría no válida. Intenta de nuevo.")
        
        continuar = input("¿Deseas registrar otro gasto? (si/no): ")

    print("\nResumen de gastos registrados:")
    for cat, total in categorias.items():
        if total > 0:
            print(f" - {cat.capitalize()}: ${total:.2f}")

# Opción 3: Mostrar resumen semanal (leer archivo)
elif opcion == 3:
    print("\nResumen semanal de registros:")
    try:
        with open(archivo, "r") as f:
            contenido = f.read()
            if contenido.strip() == "":
                print("No hay registros guardados aún.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("Aún no existe el archivo de registro. Registra un gasto o un presupuesto primero.")

# Opción no válida
else:
    print("Opción no válida. Por favor selecciona 1, 2 o 3.")
