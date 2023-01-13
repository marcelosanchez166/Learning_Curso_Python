#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal de la misma frase que ingreso, 
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

palabra=input("Escriba una palbra ")
vocal=input("Escriba una vocal ")
print(palabra.replace(vocal,vocal.upper()))
#el print esta remplazando en la  palabra que se ingreso una de las vocales de la plabra y muestra la plabra con la vocal en mayuscula
