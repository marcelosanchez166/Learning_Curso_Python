#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima
#por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.


nombre=input("Escriba su nombre ")
numero=int(input("escriba un numero por favor"))

for i in range(numero):
          print("Su nombre es ", nombre )
