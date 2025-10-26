#variables de un solo valor
numero1 = 5
numero2 = 10 #estos numeros uno por uno toma memoria

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Hola", True]

print(numeros[5]) #la lista inicia en cero, y si se pone un numero adelante dice que esta fuera de rango

frutas = ["manzana", "banana", "cereza"]
print(frutas[1]) #imprime al segundo elemento de la lista porque inicia en cero lal lista
frutas.append("naranja") #Agrega "naranja" al final de la lista 
frutas.remove("banana") #elimina "banana" de la lista
print(frutas)
frutas.remove(frutas[0]) #elimina el primer elemento de la lista