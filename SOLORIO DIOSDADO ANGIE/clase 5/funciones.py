#las funciones se recoocen como bloques de codigo que realizan una tarea especifica
#se definen con la palabra reservada def

def saludar ():
    print("hola a todos")

    def saludar_usuario(nombre, apellido, edad, ciudad, pais):

        print(f"hola {nombre}, bienvenido")

print("------------------------------------")

apellido = "diosdado"
saludar() #llamamos a la funcion
saludar_usuario("diosdado", apellido, 25, "morelia", "mexico") #podemos mandar vakores a las funciones