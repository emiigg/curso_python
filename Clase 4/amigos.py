amigos = []

for i in range(3):
    nombre = input("Ingrese el nombre de un amigo: ")
    amigos.append(nombre)
    
amigos.sort()
print("Lista de amigos en orden alfabético:")
print(amigos)

for amigo in amigos:
    print(amigo)
    
    
    