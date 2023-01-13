#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

passd=input("Ingrese su contraseña para acceder ")
contra="contra123"
if passd==contra:
          print("Bienvenido su contraseña coincide puede ingresar ")
else:
          print("Su contraseña no coincide, intentelo de nuevo ")
