#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 
#hasta ese número separados por comas.

num=int(input("Ingrese un numero Entero Positivo "))
#for i in range(1,num+1, 2):
#          print(i)

for i in range(num+1):# con el num +1 le digo que aumente una posicion para que tome el numero en dado caso se ingrese un numero impar
          if i % 2 != 0:#en la condicion entra la variable i porque la i toma la posicion de 0 asta el valor del numero que se ingresa
                    print(i, end=",")