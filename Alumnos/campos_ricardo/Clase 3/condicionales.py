# Operaciones básicas
suma = 1 + 2
resta = 1 - 1
multiplicacion = 2 * 2
division = 4 / 2

# Es igual a (==)
# No es igual a (!=)

if suma == 2:  # True o False
    print("La suma es correcta")
elif suma == 3:
    print("La suma es 3")
else:
    print("La suma es incorrecta")

print("-----------------------------")

# Comparaciones entre números
numero1 = 20
numero2 = 20

# Igual a (==)
# Mayor que (>)
# Menor que (<)
# Mayor o igual que (>=)

if numero1 > numero2:
    print("Numero 1 es mayor a numero 2")
elif numero1 < numero2:
    print("Numero 1 es menor a numero 2")
elif numero1 == numero2:
    print("Los numeros son iguales")

print("-----------------------------")

# Operadores lógicos
# and (y)
# or  (o)
# not (no)

mayoria_edad = 18

genero = input("Ingrese su genero (M/F): ")
edad = int(input("Ingrese su edad: "))

if edad >= mayoria_edad and genero.upper() == "M":
    print("Eres un hombre mayor de edad")
elif edad >= mayoria_edad and genero.upper() == "F":
    print("Eres una mujer mayor de edad")
elif edad < mayoria_edad and genero.upper() == "M":
    print("Eres un hombre menor de edad")
elif edad < mayoria_edad and genero.upper() == "F":
    print("Eres una mujer menor de edad")
else:
    print("Genero no reconocido")

print("-----------------------------")

# Ejemplo adicional de operadores lógicos combinados
condicion = True
condicion2 = False
condicion3 = True
condicion4 = True
condicion5 = False

# Combinación de operadores lógicos
resultado = (not condicion and condicion2) or condicion3 or (condicion4 and condicion5)

print("El resultado lógico de la combinación es:", resultado)
