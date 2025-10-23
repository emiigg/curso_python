while (True):
    print("Esto es un bucle infinito")
    
    if (1==1):
        break
    
print("-----------------------------")

contador = 0


while (contador <= 10):
    print("El contador es: ", contador)
    contador += 1  # contador = contador + 1
    
    
print("-----------------------------")

contador = 0
for i in range(0, 11): 
    if (i==3):
        continue
    print("El contador es: ", contador)
    contador += 1  # contador = contador + 1