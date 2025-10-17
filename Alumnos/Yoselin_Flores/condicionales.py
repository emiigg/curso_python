suma = 1 + 2
resta = 1 - 1
multiplicacion = 2 * 2
division = 4 / 2

# es igual a (==)
# no es igual a (!=)

if suma == 2: #true o false
    print("La suma es correcta")
else:
    print("La suma es incorrecta")

print("___________________________")


numero1 = 20
numero2 = 20

if numero1 > numero2:
    print("Numero 1 es mayos a Numero 2")
elif numero1 < numero2:
    print("Numero 1 es menor a Numero 2")
elif numero1 == numero2:
    print("Los numeros son iguales")


print("____________________")


GeneroMujer = F
GeneroHombre = M
MayoriaEdad = 18

genero = input("ingrese su genero (M/F)")
edad = int(input("ingrese su edad"))

if edad >= MayoriaEdad and GeneroMujer == "F":
    print("Eres una mujer de mayor edad")
elif edad >= MayoriaEdad and GeneroHombre == "M":
    print("Eres un hombre de mayor edad")
elif edad < MayoriaEdad and GeneroMujer == "F":
    print("Eres una mujer de menor edad")
elif edad < MayoriaEdad and GeneroHombre == "M":
    print("Eres un hombre de menor edad")
