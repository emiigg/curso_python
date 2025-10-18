persona = {
    "nombre": "Yoselin",
    "edad": 21,
    "cuidad": "Morelia",
    "activo": True

}
print(persona)

print(persona["nombre"]) #acceder al valor asociado a la clave "nombre"

persona = {
    "Yoselin": {
        "edad": 21,
        "cuidad": "Morelia",
        "activo": True
    },
    "Axel":{
        "edad": 22,
        "cuidad": "Cuidad de Mexico",
        "activo": False
    },
    "Ana": {
        "edad": 23,
        "cuidad": "Guadalajara",
        "activo": True
    }
}
print(persona)
