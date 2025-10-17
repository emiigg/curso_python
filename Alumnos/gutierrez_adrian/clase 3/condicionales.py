suma = 1 + 2
resta = 1 - 1
multiplicacion = 2 * 2
division = 4 / 2

if suma == 2: #aqui compara valores y solo arroja valores true o false
    print("La suma es correcta")
elif suma == 3: #termina la condicion anterior e inicia uan nueva
    print("La suma es 3")
else: #aqui termina la condicion entera
    print("La suma es incorrecta")

numero1= 10
numero2 = 20

if numero1 > numero2: 
    print("Numero 1 es mayor a numeor 2")
elif numero1 < numero2:
    print("Numero 1 es menor a numero 2")
else:
    print("Los numeros son iguales")

#operadores logicos
# and
# or
# not

genero = input("Ingrese su genero M/F: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18 and genero =='M':
    print("Eres un hombre mayor de edad")
elif edad >= 18 and genero == 'F':
    print("Eres mujer mayor de edad y")
elif edad < 18 and genero == 'M':
    print("Eres hombre menor de edad")
else:
    print("Eres mujer menor de edad")
