# Variables de un solo valor
numero1 = 5
numero2 = 10

# Lista de números
# Las listas se definen con corchetes []

numeros = [1, 2, 3, 4, 5]

print(numeros[4])  # Imprime el primer elemento de la lista

frutas = ["manzana", "banana", "cereza"]
print(frutas[1])  # Imprime el segundo elemento de la lista
frutas.append("naranja")  # Agrega "naranja" al final de la lista
print(frutas)
frutas.remove("banana")  # Elimina "banana" de la lista
print(frutas)
frutas.remove(frutas[0])  # Elimina el primer elemento de la lista
print(frutas)