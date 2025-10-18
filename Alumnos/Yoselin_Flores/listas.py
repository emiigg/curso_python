#variables de un solo valor
numero1 = 5
numero2 = 10

#listas de numeros
#las listas se definen con corchetes[]

numeros = [1, 2, 3, 4, 5]

print(numeros[4]) #imprime el primer elemento de la lsia

frutas = ["manzana", "banana", "cereza"]
print(frutas[1]) #imprime el segundo elemento de la lista
frutas.append("naranja") #agrega "naranja" al final de la lista
print(frutas)
frutas.remove("banana") #elimina "banana" de la lista
print(frutas)
frutas.remove(frutas[0]) #elimina el primer elemento de la lista
print(frutas)