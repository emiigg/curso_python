
# MENÚ DE TIENDA 
# ====================

def crear_inventario():
    try:
        archivo = open("inventario.txt", "r", encoding="utf-8")  # intento abrir el inventario
        archivo.close()
    except FileNotFoundError:  # si no existe, lo creo
        archivo = open("inventario.txt", "w", encoding="utf-8")
        archivo.write("Producto,Precio,Cantidad\n")  # pongo los encabezados
        archivo.close()


def agregar_producto():
    crear_inventario()  # me aseguro que exista el inventario antes de agregar
    try:
        nombre = input("Nombre del producto: ")  
        precio = float(input("Precio: "))        
        cantidad = int(input("Cantidad: "))      
        # agrego el producto al inventario
        with open("inventario.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{precio},{cantidad}\n")
        print("Producto agregado correctamente.\n")
    except ValueError:
        print("Error: datos inválidos.\n")  # aviso si el precio o cantidad no son números


def mostrar_inventario():
    print("\n=== INVENTARIO ===")
    try:
        # leo todo el inventario
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if len(lineas) <= 1:  # si solo está el encabezado
            print("No hay productos en el inventario.")
        else:
            print("Producto | Precio | Cantidad")
            # muestro todos los productos
            for i in range(1, len(lineas)):
                datos = lineas[i].strip().split(",")  # separo nombre, precio y cantidad
                print(datos[0], "|", "$" + datos[1], "|", datos[2])
    except:
        print("No se pudo leer el inventario.")
    print("==================\n")


def vender_producto():
    crear_inventario()  # que exista el inventario antes de vender
    producto = input("Producto a vender: ")  # pido el producto que quiere vender
    
    try:
        cantidad_vendida = int(input("Cantidad a vender: "))  # cantidad
    except ValueError:
        print("Error: cantidad inválida.")
        return

    try:
        # leo el inventario
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        nuevo_contenido = "Producto,Precio,Cantidad\n"  # voy a armar el inventario actualizado
        venta_exitosa = False
        producto_encontrado = False
        total = 0

        # recorro todos los productos
        for i in range(1, len(lineas)):
            datos = lineas[i].strip().split(",")
            nombre = datos[0]
            precio = float(datos[1])
            cantidad = int(datos[2])

            if nombre.lower() == producto.lower():  # si el producto coincide
                producto_encontrado = True
                if cantidad_vendida <= cantidad:  # si hay suficiente
                    cantidad -= cantidad_vendida  # resto la cantidad vendida
                    total = cantidad_vendida * precio  
                    venta_exitosa = True
                    print(f"Venta realizada. Total: ${total}")
                else:
                    print("No hay suficiente cantidad de ese producto.")

            # solo agrego productos si > 0
            if cantidad > 0:
                nuevo_contenido += f"{nombre},{precio},{cantidad}\n"

        if not producto_encontrado:  # si no lo encontre
            print("El producto no está en el inventario.")
        else:
            # actualizo el inventario
            with open("inventario.txt", "w", encoding="utf-8") as archivo:
                archivo.write(nuevo_contenido)

            # guardo la venta si sí
            if venta_exitosa:
                with open("ventas.txt", "a", encoding="utf-8") as ventas:
                    ventas.write(f"{producto},{cantidad_vendida},{total}\n")

    except Exception as e:
        print("Error al realizar la venta:", e)


def ver_ventas():
    print("\n=== HISTORIAL DE VENTAS ===")
    try:
        # leo   las ventas
        with open("ventas.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()

        if len(lineas) == 0:  # si no hay ventas
            print("No hay ventas registradas.")
        else:
            print("Producto | Cantidad | Total")
            # muestro todas las ventas
            for linea in lineas:
                datos = linea.strip().split(",")
                print(datos[0], "|", datos[1], "|", "$" + datos[2])
    except FileNotFoundError:  # si el archivo de ventas no existe
        print("No hay ventas registradas.")
    except:
        print("No se pudo leer el archivo de ventas.")
    print("============================\n")


def menu():
    crear_inventario()  # me aseguro que exista el inventario 
    while True:
        print("""
=====================
      MENÚ TIENDA
=====================
1. Mostrar inventario
2. Agregar producto
3. Vender producto
4. Ver ventas
5. Salir
""")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_inventario()  
        elif opcion == "2":
            agregar_producto()  
        elif opcion == "3":
            vender_producto() 
        elif opcion == "4":
            ver_ventas()  
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.\n")  # aviso si ponen algo que no es del menú


menu()  # inicio el programa
