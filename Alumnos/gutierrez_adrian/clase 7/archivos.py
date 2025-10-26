from pathlib import Path
#"r" es para read
#"w" es para write y si el archivo no existe lo crea, si existe lo sobreescribe 
#"x" create y si el archivo ya existe lanza un error
#"a" append (añadir) si el archivo no existe lo crea

ruta = Path("datos.txt")

with ruta.open("a", encoding="utf-8") as archivo:
    archivo.write("Hola desde Python\n")
    archivo.writable("Segunda linea escrita\n")

archivo.open("r", encoding="utf-8")
archivo.write("Tercera linea escrita\n")
