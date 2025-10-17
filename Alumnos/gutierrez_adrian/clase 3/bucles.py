while (True):
    print("esto es un bucle infinito")

    if (1==1): #esto es una condicion de parada
        break

contador = 0

while (contador <= 10 ):
    print("El contador es: ", contador)
    contador += 1 #esto es: contador = contador + 1

for i in range(0, 11): #el range determina cuando debe de termianr el ciclo
    print ("el copntador es: ", contador)
    contador += 1
for i in range(0, 11):
    if (i==3):
        break #esto me indica que debe de terminar cuando i e sigual a 3 y se podria usar continue para que siga el ciclo
    print ("el copntador es: ", contador)
    contador += 1
