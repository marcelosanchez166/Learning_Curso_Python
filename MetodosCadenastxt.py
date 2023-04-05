#Uso de metodos para cadenas STRING

#METODOS MAS UTILIZADOS

"""
upper()= convierte en mayusculas las letras de un string
lower()=convierte en minusculas las letras de un string
capitalize()=pone la primera letra en mayusculas
count()=contar cuantas veces hay una letra oo una cadena de caracteres depende lo que necesite
find()=buscar la posicicion de un caracter o una cadena
isdigit()=devuelbe un boolean True or False, nos dice si el valor introducido es un digito o no 
isalum()=Comprueba si lo que se ingreso es alfanumerico
isalpha()=Comprueba si hay solo letras, los espacios no cuentan
split()=separa las palabras utilizando espacios
strip()=borra los espacios sobrantes al inicio y al final
replace()=cambia una palabra o una letra por otra
rfind()=busca la posicicion de un caracter o una palabra desde el final
"""

#Eje

edad=input("Ingrese su edad: ")

while edad.isdigit()==False:
        print("Por favor ingresa en numero tu edad: ")
        edad=input("Ingrese su edad: ")

if (int(edad)<18):
        print("No eres mayor de edad no puede pasar ")
else:
        print("Eres mayor de edad puedes pasar ")