persona = {
    "nombre": "Emiliano",
    "edad": 23,
    "ciudad": "Morelia",
    "activo": True
}

print(persona)


print(persona["nombre"])  # Acceder al valor asociado a la clave "nombre"


personas = {
    "Emiliano": {
        "edad": 23,
        "ciudad": "Morelia",
        "activo": True
    },
    "Ana": {
        "edad": 30,
        "ciudad": "Ciudad de México",
        "activo": False
    },
    "Christopher": {
        "edad": 28,
        "ciudad": "Guadalajara",
        "activo": True
    }
}

print(personas["Ana"]["ciudad"])  # Acceder a la ciudad de Ana