from pathlib import Path

# "r" Leer (read)
# "w" Escribir (write) - si el archivo no existe lo crea, si existe lo sobreescribe
# "x" Crear (create) - si el archivo ya existe lanza un error
# "a" Añadir (append) - si el archivo no existe lo crea


ruta = Path("datos.txt")

"""
with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("Hola desde Python")
    archivo.write("Segunda línea escrita)"""
 
 
#with open("datos.txt", "r", encoding="utf-8") as archivo:
 #   contenido = archivo.read()
  #  print(contenido)
    
"""   
archivo = open("datos.txt", "r")
archivo.write("Tercera línea escrita")
archivo.close()"""


# FileNotFoundError: [Errno 2] No such file or directory: 'datos.txt'
# PermissionError: [Errno 13] Permission denied: 'datos.txt'
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte


try:
    with ruta.open("w", encoding="utf-8") as archivo:
        """contenido = archivo.read()
        print(contenido)"""
        pass
        
except FileNotFoundError:
    with ruta.open("a", encoding="utf-8") as archivo:
        archivo.write("Archivo creado porque no existía.")
        
    print("El archivo no existia, se ha creado uno nuevo.")