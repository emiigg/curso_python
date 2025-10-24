# Que es programar?
"""

DIA 1 - Repaso de conceptos básicos
Darle instrucciones a la computadora
    -> Lograr un objetivo:
        Algoritmo: Conjunto de instrucciones ordenadas y finitas para resolver un problema o realizar una tarea específica.
        - Hacer un Sandwich
        - Lavar la ropa

"""

print("-------VARIABLES Y TIPOS DE DATOS-------")

numero = 10
texto = "Hola, soy un texto"
flotante = 3.14
booleano = True  # (True o False)


print("-------OPERACIONES BÁSICAS-------")
suma = 1 + 2
resta = 5 - 3
multiplicacion = 4 * 2
exponte = 2 ** 3  # 2^3 = 2*2*2 = 8
division = 10 / 2 # = 5.0
division_entera = 10 // 3 # (/ = 3.3333...) (// = 3)
modulo = 10 % 3  # Residuo de la división (10 dividido 3 da 3, residuo 1)


print("-------OPERADORES LÓGICOS-------")

condicion1


# AND (y)
condicion1 and condicion2# True si ambas son verdaderas
# Si una sola es falsa, el resultado es False

# OR (o)
condicion1 or condicion2 # True si al menos una es verdadera
# Solo es False si ambas son falsas

# NOT
not condicion1 # Invierte el valor de la condición


print("-------CONDICIONALES-------")

# Igualdad
1 == 1  # True
1 == 2  # False
# Desigualdad
1 != 2  # True
1 != 1  # False


# Mayor que / Menor que
1 > 0  # True
1 < 0  # False

# Mayor o igual / Menor o igual
1 >= 1  # True
1 <= 0  # False



print("-------CONDICIONES-------")

if condicion:
    # Bloque de código si la condición es verdadera
    pass
elif condicion2:
    # Bloque de código si la condición2 es verdadera
    pass
else:
    # Bloque de código si ninguna condición es verdadera
    pass

condicion1 = False

if not condicion1:
    print("La condición1 es falsa")

print("-------BUCLES-------")

while condicion:
    # Bloque de código que se repite mientras la condición sea verdadera
    
    # Definir condiciones de parada para evitar bucles infinitos.
    pass

while True:
    # Bucle infinito (ejemplo)
    break  # Rompe el bucle inmediatamente


for i in range(5):
    # Bloque de código que se repite 5 veces (i toma valores de 0 a 4)
    # 0, 1, 2, 3, 4
    if i == 3:
        continue  # Salta a la siguiente iteración cuando i es 3
    print(i)
    # 0, 1, 2, 4

# Para detener un bucle antes de que termine de iterar usamos 'break'
# Para saltar a la siguiente iteración usamos 'continue'


print("-------LISTAS, TUPLAS Y DICCIONARIOS-------")

# Listas
mi_lista = [1, 2, 3, 4, 5, "Hola", True, 3.14] 
numeros = [10, 20, 30, 40, 50]#,60

numeros.append(60)  # Agrega 60 al final de la lista
#numero = [10, 20, 30, 40, 50, 60]
numeros.remove(20)  # Elimina el primer 20 que encuentra
#numero = [10, 30, 40, 50, 60]
len(numeros)  # Devuelve la cantidad de elementos en la lista (5)

# Tuplas
tupla_numeros = (1, 2, 3, 4, 5)
# tupla_numeros.append(6)  # Error: las tuplas son inmutables
len(tupla_numeros)  # Devuelve la cantidad de elementos en la tupla (5)


# numeros[0] = 10
# tupla_numeros[3] = 4 


# Diccionarios
mi_diccionario = {
    "clave1": 1,
    "clave2": "valor2",
    "clave3": [1, 2, 3],
    "diccionario_interno": {
        "subclave1": True,
        "subclave2": 3.14,
        "diccionario_mas_interno": {
            "otra_subclave": "Hola"
        }
    }
}
    
mi_diccionario["clave3"] # Devuelve [1, 2, 3]
mi_diccionario["diccionario_interno"]# Devuelve el diccionario interno
"""
{
    "subclave1": True,
        "subclave2": 3.14,
        "diccionario_mas_interno": {
            "otra_subclave": "Hola"
        }
}
"""


print("-------FUNCIONES-------")

def mi_funcion():
    print("Hola desde mi función")
    
mi_funcion()  # Llamada a la función


def sumar(a, b):
    suma = a + b
    
    return suma
    
def restar(a, b):
    resta =  a - b
    
    return resta

a = 10
b = 5
suma = sumar(a, b)

def division(a, b):
    return a / b

# 1/0 = Error

print("-------EXCEPCIONES-------")

# DIVISION POR CERO
try:
    resultado = division(10, 0)
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
except:
    print("Ocurrió un error inesperado.")
    
    
print("-------PERSISTENCIA DE DATOS-------")

# Trabando con archivos

# MODOS PARAR ABRIR ARCHIVOS
# "r" -> Modo lectura (por defecto). Error si el archivo no existe.
# "w" -> Modo escritura. Crea un archivo nuevo o sobrescribe uno existente.
# "a" -> Modo anexar. Agrega contenido al final del archivo o crea uno nuevo si no existe.
try:
    # with open("ruta al archivo", "modo") as variable_de_archivo:
    
    
    with open("archivo_ejemplo.txt", "w") as archivo:
        archivo.write("Hola, este es un archivo de ejemplo.\n")
        archivo.write("Estamos aprendiendo sobre persistencia de datos en Python.\n")
        
    with open("archivo_ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
        """
            Hola, este es un archivo de ejemplo.
            Estamos aprendiendo sobre persistencia de datos en Python.
        """
except Exception as e:
    print(f"Ocurrió un error al manejar el archivo: {e}")
    
    
# Cuando trabajamos con archivos, es importante manejar excepciones para evitar errores inesperados.