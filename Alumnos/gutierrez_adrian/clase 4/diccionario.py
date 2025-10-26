persona = {
    "nombre": "adrian",
    "edad": 20,
    "ciudad": "moroleon"
}
#siempre los nombres deben de ir con comillas, y la derecha solo cuando sea strin

print(persona) #aqui imprime todo el diccionario

print(persona["ciudad"]) #aqui solo imprime el valor solicitado

#diccionario de diccionarios

personas = {
    "Adrian": {
        "ciudad": "moroleon",
        "edad": 20
    },
    "Diana": {
        "ciudad": "moroleon",
        "edad": 20
    },
    "joel": {
        "ciudad": "morelia",
        "edad": 24
    }
    
}

print(personas ["Adrian"]["ciudad"]) #el primer corchete abre la persona elegida y el segundo la opcion mas especifica
