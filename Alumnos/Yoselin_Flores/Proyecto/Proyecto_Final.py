import random
ArchivoP = "Puntos.txt"

def GuardarPuntos():
    Puntos = {}
    with open(ArchivoP, "a+") as Archivo:
        Archivo.seek(0)
        for linea in Archivo:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                User = partes[0]
                puntos = int(partes[1])
                Puntos[User] = puntos
    return Puntos

def AlmacenarPuntaje(User, PuntosNuevos):
    puntos = GuardarPuntos()
    if User not in puntos or PuntosNuevos < puntos[User]:
        print(f"Lograste un nuevo record {User}: {PuntosNuevos} intentos ")
        puntos[User] = PuntosNuevos
        with open(ArchivoP, "w") as Archivo:
            for US, PU in puntos.items():
                Archivo.write(f"{US},{PU}\n")
    else:
        print(f"Tu puntaje es de {PuntosNuevos}. El record ahora es de {puntos[User]}")

def VerPuntaje():
    Puntaje = GuardarPuntos()
    if not Puntaje:
        print("\n No existe el puntaje")
        return
    print("\n Puntajes guardados")
    OrdPuntaje = sorted(Puntaje.items(), key=lambda item: item[1])
    for User, Puntos in OrdPuntaje:
        print(f"{User}: {Puntos}")
    print("_")

def GradoDeDificultad():
    print("\n Elige el grado de dificultad")
    print("1. Facil num. del 1 al 10")
    print("2. Medio num. del 1 al 50")
    print("3. Dificil num. del 1 al 100")
    while True:
        Op = input("Escriba 1, 2 o 3")
        if Op == "1":
            return 10
        elif Op == "2":
            return 50
        elif Op == "3":
            return 100
        else:
            print("Error, inetente otra vez")

def Pista(Numero, intento):
    resta = abs(Numero - intento)
    if resta <= 2:
        return "demasiado caliente"
    elif resta <= 5:
        return "caliente"
    elif resta <= 10:
        return "Se esta enfriamdo"
    elif resta <= 20:
        return "frio"
    else:
        return "congelado"

def Juega_Adivina_El_Numero(User):
    LimSuperior = GradoDeDificultad()
    Num_A_Encontrar = random.randint(1, LimSuperior)
    Attempts = 0
    Acertado = False 
    print(f"\n Elegi un número entre 1 y {LimSuperior}. Adivina cual es: ")
    while not Acertado:
        try: 
            Attempts_str = input("Escribe su intento: ")
            Intento = int(Attempts_str)
            Attempts += 1
            if Intento < 1 or Intento > LimSuperior:
                print(f"Escribe un número entre 1 y {LimSuperior}.")
                continue
            if Intento == Num_A_Encontrar:
                Acertado = True
                print(f"Felicidades, {User} adivinaste el número en {Attempts} intentos!")
            else:
                pista = Pista(Num_A_Encontrar, Intento)
                print(pista)
        except ValueError:
            print("Error. Escribe otro numero ")
    AlmacenarPuntaje(User, Attempts)

def menu_principal():
    print("Hola, este es el juego de Adivina el Numero")
    User = input("Escribe su nombre de usuario: ")
    while True:
        print(f"\n Usuario Actual: {User} ")
        print("Elija una opción:")
        print("1. Jugar Adivina el Número")
        print("2. Ver Puntajes")
        print("3. Salir")
        OP = input("Elige una opción (1-3): ")
        if OP == "1":
            Juega_Adivina_El_Numero(User)
        elif OP == "2":
            VerPuntaje()
        elif OP == "3":
            print(f"Gracias por jugar, {User}. ")
            break
        else:
            print("Error. Intenta otra vez")

if __name__ == "__main__":
    menu_principal()