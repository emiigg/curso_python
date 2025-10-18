def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado
def multiplicar(a, b):
    resultado = a * b
    return resultado
def dividir(a, b):
    resultado = a / b
    return resultado

def imprint_menu():
    print("== menu de calculadora==")
    print("1, sumar")
    print("2, restar")
    print("3, multiplicar")
    print("4, dividir")
    print("5, salir")

def obtener_numeros():
    a = float(input("ingresa el primer numero: "))
    b = float(input("ingrsa el segundo numero: "))

    return a, b

while True:
    imprimir_menu()

    opcion = input("elige una opcion: ")
    numero1, numero2 = obtener_numeros()

    if opcion == "1":

        print({"el resultado de la suma es: {sumar(numero1, numero2)}"})
    elif opcion == "2":
         print({"el resultado de la resta es: {restar(numero1, numero2)}"})
    elif opcion == "3":
         print({"el resultado de la multiplicacion es: {multiplicar(numero1, numero2)}"})
    elif opcion == "4":
         print({"el resultado de la division es: {dividir(numero1, numero2)}"})
    elif opcion == "5":
        print("hasta luego")
        break




