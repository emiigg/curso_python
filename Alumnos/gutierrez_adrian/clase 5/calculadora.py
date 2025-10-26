def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a -b
    return resultado

def multiplicar(a, b):
    resultado = a*b
    return resultado

def dividir(a, b):
    resultado = a/b
    return resultado

def imprimir_menu():
    print("MENU DE CALCULADORA")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def obtener_numeros():
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero"))

while True:
    imprimir_menu()

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Hasta Luego")
        break
    elif opcion not in ["1", "2", "3", "4"]:
        print("Opcion no valida. Intente de nuevo.")
        continue

    numero1, numero2 = obtener_numeros()

    if opcion == "1":
        print(f"El resultado de la suma es: {sumar(numero1, numero2)}") #de esta manera manda a llamar la funcion y las variables dentro de los parentesis son las que usa para lo que se haya definido
    
    elif opcion == "2":
        print(f"El resultado de la restar es: {restar(numero1, numero2)}")
    
    elif opcion == "3":
        print(f"El resultado de la multiplicacion es: {multiplicar(numero1, numero2)}")
    
    elif opcion == "4":
        print(f"El resultado de la division es: {dividir(numero1, numero2)}")

