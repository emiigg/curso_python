pesona =  {
    "nombre": "Daniel", 
    "apellido": "Gomez", 
    "edad": 25,
    "ciudad": "Madrid"
    }

print(pesona["nombre"]) # Acceder al valor de la clave "nombre"
print(pesona.get("edad")) # Acceder al valor de la clave "edad"

#Se puede tener un diccionario dentro de otro diccionario
peronas = {
    "Daniel": {"apellido": "Gomez", "edad": 25, "ciudad": "Madrid"},
    "Ana": {"apellido": "Lopez", "edad": 30, "ciudad": "Barcelona"},
    "Luis": {"apellido": "Martinez", "edad": 28, "ciudad": "Valencia"}
}