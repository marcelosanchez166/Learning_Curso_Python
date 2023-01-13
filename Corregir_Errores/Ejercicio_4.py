"""Detectar y corregir los errores del siguiente programa que devuelve y 
elimina el teléfono de un listín telefónico a través del nombre del usuario:"""

listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(usuario):
    del listin[usuario]
    return listin

print(elimina("Juan"))



