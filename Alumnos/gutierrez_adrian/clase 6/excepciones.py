#las excepciones son errores que detienen el flujo del programa
#un error comun es dividir entre 0
# numero = int("s") este un tipo de error de valor y en la terminal tambien te dice en donde se encuentra el error

#una solucion es el try except
"""
try: 
    numero = int(input("Ingrese un numero"))
    division  = 10 / numero
    print(f"el resultado de la division es: {division}")

except ZeroDivisionError: #aqui se debe de poner el tipo de error a cachar
    print("Error: No se puede dividir entre cero.")

finally:
    print("Esta linrea siempre se imprime") #esto siempre se imprime independientemente de la parte de arriba

"""
"""
while True: 
    try:
        n = int(input("Ingresa un número: "))
        print(10 / n)
    except ValueError:
        print("Error: Debes de ingresar un número válido.")
    
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.") #se puede meter mas de un except
    
    finally:
        print("Intento de división finalizado")
"""
try: 
    n = int(input("Ingresa un número: "))
    print(10 / n)

except Exception as e: #si el except esta solo, atrapa cualquier error sin tener que definirlo, el Exception me define cual fue el error y se guarda en la variable e
    print("Error: ", e)