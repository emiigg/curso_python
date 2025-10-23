from pathlib import Path

# Ruta completa con nombre de archivo
ruta = Path("Ruta")

# 
with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("Segunda\n")
    archivo.write("Hola\n")

try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
     contenido=archivo.read()
     print(contenido)
except FileNotFoundError:
   with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("Archivo creado exitosamente\n")

print("El archivo no exitia")