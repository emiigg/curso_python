def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def imprimir_menu():
    print("=== MENU DE OPCIONES ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def optener_numeros():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    return a, b

# Bucle principal
while True:
    imprimir_menu()
    opcion = input("Elige una opcion: ")

    if opcion in ["1", "2", "3", "4"]:
        numero1, numero2 = optener_numeros()

    if opcion == "1":
        print(f"El resultado de la suma es: {sumar(numero1, numero2)}")
    elif opcion == "2":
        print(f"El resultado de la resta es: {restar(numero1, numero2)}")
    elif opcion == "3":
        print(f"El resultado de la multiplicacion es: {multiplicar(numero1, numero2)}")
    elif opcion == "4":
        print(f"El resultado de la division es: {dividir(numero1, numero2)}")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion invalida. Intenta de nuevo.")


