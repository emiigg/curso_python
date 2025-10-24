import sys

# Estructura de datos para almacenar el presupuesto
# Inicialmente vacía para que el usuario la configure.
presupuesto = {
    "ingreso_mensual": 0.0,
    "gastos_registrados": {}, # Almacena {Categoría: Monto Gastado}
    # Mapeo de categorías a los 3 tipos de gasto definidos
    "tipo_categoria": {
        "Alquiler/Hipoteca": "Fijos",
        "Suscripciones (Netflix, Spotify, etc.)": "Fijos",
        "Pagos de Préstamos/Deudas": "Fijos",
        "Comida/Supermercado": "Necesarios Variables",
        "Servicios (Luz, Agua, Internet, Teléfono)": "Necesarios Variables",
        "Transporte/Gasolina": "Necesarios Variables",
        "Cuidado Personal/Salud": "Necesarios Variables",
        "Gimnasio/Actividad Física": "Opcionales/Plus",
        "Entretenimiento/Ocio (Cine, Salidas)": "Opcionales/Plus",
        "Ropa y Accesorios": "Opcionales/Plus",
        "Viajes/Vacaciones": "Opcionales/Plus",
        "Ahorro/Inversión": "Opcionales/Plus" # Aunque es un "plus", es una excelente práctica
    }
}

# --- Funciones de Utilidad ---

def obtener_categorias_por_tipo(tipo):
    """Devuelve una lista de categorías que pertenecen al tipo de gasto especificado."""
    return [cat for cat, t in presupuesto["tipo_categoria"].items() if t == tipo]

def mostrar_menu_categorias():
    """Muestra todas las categorías disponibles y su tipo."""
    print("\n--- Categorías Disponibles ---")
    tipos = ["Fijos", "Necesarios Variables", "Opcionales/Plus"]

    for i, tipo in enumerate(tipos):
        categorias = obtener_categorias_por_tipo(tipo)
        print(f"\n[{i+1}] {tipo} (Gastos {tipo.split('/')[0]})")
        for j, cat in enumerate(categorias):
            print(f"    {j+1}. {cat}")

def inicializar_gastos_registrados():
    """Inicializa los gastos registrados a cero para todas las categorías."""
    for cat in presupuesto["tipo_categoria"].keys():
        presupuesto["gastos_registrados"][cat] = 0.0

# --- Funciones de Menú ---

def configurar_ingreso():
    """Permite al usuario ingresar o actualizar su ingreso mensual."""
    while True:
        try:
            ingreso = float(input("\n¿Cuál es tu ingreso o ganancia mensual total? (Ej. 2500.50): $"))
            if ingreso < 0:
                print("El ingreso no puede ser negativo. Inténtalo de nuevo.")
                continue
            presupuesto["ingreso_mensual"] = ingreso
            # Inicializamos todos los contadores de gasto a 0 al configurar el ingreso.
            inicializar_gastos_registrados()
            print(f"¡Ingreso mensual de ${ingreso:.2f} registrado con éxito!")
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

def registrar_gasto():
    """Permite al usuario registrar un nuevo gasto en una categoría existente."""
    if presupuesto["ingreso_mensual"] == 0.0:
        print("\n🚫 ERROR: Primero debes configurar tu ingreso mensual (Opción 1).")
        return

    categorias_disponibles = list(presupuesto["tipo_categoria"].keys())
    
    while True:
        mostrar_menu_categorias()
        print("\n[Añadir] para añadir una nueva categoría.")
        print("[Volver] para regresar al menú principal.")

        opcion = input("Ingresa el nombre completo de la categoría donde quieres registrar el gasto: ").strip()

        if opcion.lower() == "volver":
            return
        
        if opcion.lower() == "añadir":
            nombre_nueva_cat = input("Ingresa el nombre de la nueva categoría: ").strip()
            if not nombre_nueva_cat:
                print("El nombre de la categoría no puede estar vacío.")
                continue

            print("\nSelecciona el tipo de gasto para esta nueva categoría:")
            print("1. Fijos (Ej: Alquiler)")
            print("2. Necesarios Variables (Ej: Comida)")
            print("3. Opcionales/Plus (Ej: Entretenimiento)")
            
            tipo_opcion = input("Ingresa el número de tipo (1, 2, o 3): ")
            tipos_map = {"1": "Fijos", "2": "Necesarios Variables", "3": "Opcionales/Plus"}
            
            if tipo_opcion in tipos_map:
                tipo_gasto = tipos_map[tipo_opcion]
                presupuesto["tipo_categoria"][nombre_nueva_cat] = tipo_gasto
                presupuesto["gastos_registrados"][nombre_nueva_cat] = 0.0
                categorias_disponibles.append(nombre_nueva_cat)
                print(f"✅ Categoría '{nombre_nueva_cat}' ({tipo_gasto}) añadida con éxito.")
                continue
            else:
                print("Opción de tipo inválida.")
                continue


        if opcion in categorias_disponibles:
            categoria_seleccionada = opcion
            break
        else:
            print(f"Categoría '{opcion}' no encontrada. Por favor, intenta de nuevo o revisa la ortografía.")
            

    while True:
        try:
            monto = float(input(f"¿Cuánto gastaste en '{categoria_seleccionada}'? $: "))
            if monto <= 0:
                print("El monto debe ser positivo.")
                continue
            
            # Registrar y acumular el gasto
            presupuesto["gastos_registrados"][categoria_seleccionada] += monto
            print(f"✅ Gasto de ${monto:.2f} registrado en '{categoria_seleccionada}'.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido para el monto.")

def mostrar_reporte():
    """Imprime un reporte detallado del estado financiero mensual."""
    print("\n" + "="*50)
    print("        📊 REPORTE DE GASTOS MENSUAL 📊")
    print("="*50)

    ingreso = presupuesto["ingreso_mensual"]
    total_gastado = sum(presupuesto["gastos_registrados"].values())
    
    print(f"💰 Ingreso Mensual Registrado: ${ingreso:.2f}")
    print(f"💸 Total Gastado este mes:     ${total_gastado:.2f}")
    
    saldo_restante = ingreso - total_gastado
    
    # Determinar el color del saldo
    if saldo_restante >= 0:
        print(f"🟢 Saldo Restante:              ${saldo_restante:.2f}")
    else:
        print(f"🔴 ¡Advertencia! Saldo Negativo: ${saldo_restante:.2f}")

    print("-" * 50)
    print("DETALLE POR TIPO DE GASTO Y CATEGORÍA")
    print("-" * 50)

    tipos = ["Fijos", "Necesarios Variables", "Opcionales/Plus"]
    
    for tipo in tipos:
        categorias = obtener_categorias_por_tipo(tipo)
        total_por_tipo = 0.0
        
        print(f"\n>>> TIPO DE GASTO: {tipo.upper()}")
        
        for cat in categorias:
            monto = presupuesto["gastos_registrados"].get(cat, 0.0)
            if monto > 0:
                print(f"    - {cat}: ${monto:.2f}")
                total_por_tipo += monto
        
        if total_por_tipo == 0 and any(c in presupuesto["gastos_registrados"] for c in categorias):
             print(f"    (Aún no hay gastos registrados en las categorías {tipo})")

        print(f"  TOTAL {tipo.upper()}: ${total_por_tipo:.2f}")
    
    print("\n" + "="*50)

def menu_principal():
    """Función principal que maneja el menú del programa."""
    
    # Inicialización, si el programa corre por primera vez
    inicializar_gastos_registrados()

    print("¡Bienvenido al Control de Gastos Mensual!")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. 💰 Configurar/Actualizar Ingreso Mensual")
        print("2. 📝 Registrar Nuevo Gasto")
        print("3. 📊 Mostrar Reporte de Gastos")
        print("4. 🚪 Salir")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            configurar_ingreso()
        elif opcion == '2':
            registrar_gasto()
        elif opcion == '3':
            mostrar_reporte()
        elif opcion == '4':
            print("\n¡Gracias por usar el Control de Gastos! ¡Hasta pronto!")
            sys.exit() # Salir del programa
        else:
            print("Opción no válida. Por favor, selecciona un número del 1 al 4.")

if __name__ == "__main__":
    menu_principal()
