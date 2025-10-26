amigos = []

for i in range(3):
    nombre = input("ingrese el nombre de un amigo: ")
    amigos.append(nombre)

amigos.sort()
print("lista de amigos en orden alfabetico")
print(amigos)

for amigo in amigos:
    print(amigo)

