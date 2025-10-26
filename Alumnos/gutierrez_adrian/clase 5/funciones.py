def saludar():
    print("Hola. Bienvenido al sistema de calificaciones.")

def saludar_usuario(nombre, apellido, edad, ciudad, pais): #dentro del parentesis se manda a llamar alguna variable
    print(f"Hola, {nombre} bienvenido al sistema de calificaciones.")

print("---------------")

apellido = "Gtz"
saludar()
saludar_usuario("Adrian", apellido, 25, "Moroleon", "mexico") #si importa el orden ya que si se pone apellido en nombre, va a mostrar en nombre el apellido


