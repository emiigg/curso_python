#division = 2/0 

#numero = int("s")

"""
try:
    numero = int(input("Ingresa un número: "))
    division = 10 / numero
    print(f"El resultado de la división es: {division}")
except ZeroDivisionError:
    print("Infinito")

finally:
    print("Esta linea siempre se imprime.")
    
    """
    
print("-----------------------------------------------------------")
   
    
while True: 
    try:
        n = int(input("Ingresa un número: "))
        print(10 / n)
        
    except (ValueError, ZeroDivisionError) as e:
        print("Error: ", e)
    
    except Exception as e:
        print("Error desconocido: ", e)
    
    finally:
        print("Intento de división finalizado.")
        print("-----------------------------------------------------------")
        

