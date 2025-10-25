inventario = {}
ventas = []

while True:
    print("\n TIENFUTA DE DONIA CHONA")
    print("1. Vender producto")
    print("2. Agregar producto")
    print("3. Ver inventario")
    print("4. Salir")
    
    opcion = input("Elige opción: ")
    
    if opcion == "1":
        print("\n---VENDER")
        if not inventario:
            print("No hay productos en inventario")
            continue
        print("Productos disponibles:")
        for producto, datos in inventario.items():
            print(f"- {producto}: ${datos['precio']} (Stock: {datos['cantidad']})")
        
        producto = input("Producto a vender: ")
        
        if producto not in inventario:
            print("Producto no existe")
            continue
            
        if inventario[producto]['cantidad'] <= 0:
            print("No hay stock")
            continue
            
        try:
            cantidad = int(input("Cantidad: "))
            
            if cantidad <= 0:
                print("Cantidad debe ser mayor a 0")
                continue
                
            if cantidad > inventario[producto]['cantidad']:
                print(f"Solo hay {inventario[producto]['cantidad']} unidades")
                continue
            precio = inventario[producto]['precio']
            total = precio * cantidad
            
            inventario[producto]['cantidad'] = inventario[producto]['cantidad'] - cantidad
            
            ventas.append({
                'producto': producto,
                'cantidad': cantidad,
                'total': total
            })
            
            print(f"Venta exitosa! Total: ${total}")
            
        except:
            print("Error en cantidad")
    
    elif opcion == "2":
        print("\n---AGREGAR PRODUCTO")
        
        producto = input("Nombre producto: ")
        
        try:
            precio = float(input("Precio: $"))
            cantidad = int(input("Cantidad: "))
            
            if precio <= 0 or cantidad < 0:
                print("Precio y cantidad deben ser positivos")
                continue
                
            if producto in inventario:
                inventario[producto]['cantidad'] = inventario[producto]['cantidad'] + cantidad
                print(f"Actualizado: {producto} +{cantidad} unidades")
            else:
                inventario[producto] = {
                    'precio': precio,
                    'cantidad': cantidad
                }
                print(f"Producto {producto} agregado")
                
        except:
            print("Error en datos")
    
    elif opcion == "3":
        print("\n---INVENTARIO")
        
        if not inventario:
            print("Inventario vacío")
            continue
            
        total_valor = 0
        for producto, datos in inventario.items():
            valor = datos['precio'] * datos['cantidad']
            total_valor = total_valor + valor
            print(f"{producto}: ${datos['precio']} | Stock: {datos['cantidad']} | Valor: ${valor}")
        
        print(f"VALOR TOTAL INVENTARIO: ${total_valor}")
        
    elif opcion == "4":
        print("Byeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee (ya se cerró el programa)")
        break
    
    else:
        print("Opción no válida")