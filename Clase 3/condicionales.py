suma = 1 + 2
resta = 1 - 1
multiplicacion = 2 * 2
division = 4 / 2


# Es iugal a (==)
# No es igual a (!=)

if suma == 2:  #True o False
    print("La suma es correcta")
elif suma == 3:
    print("La suma es 3")
else:
    print("La suma es incorrecta")

    
print("-----------------------------")


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

# Operadores logicos
# and (y)
# or  (o)
# not (no)


mayoria_edad = 18

genero = input("Ingrese su genero (M/F): ")
edad = int(input("Ingrese su edad: "))

if edad >= mayoria_edad and genero == "M":
    print("Eres un hombre mayor de edad")
elif edad >= mayoria_edad and genero == "F":
    print("Eres una mujer mayor de edad")
elif edad < mayoria_edad and genero == "M":
    print("Eres un hombre menor de edad")
elif edad < mayoria_edad and genero == "F":
    print("Eres una mujer menor de edad")
    
    
(not condicion and condicion2) or condicion3 or (condicion4 and condicion5)
