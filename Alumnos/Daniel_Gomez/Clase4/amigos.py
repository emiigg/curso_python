amigos = []
for i in range(3):
    nombre = input("Ingrese el nombre del amigo: ")
    amigos.append(nombre)

amigos.sort()
print("Lista de amigos ordenada:")
print(amigos)

for amigo in amigos:
    print(amigo)