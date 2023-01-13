#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar
number=int(input("Escriba un numero cualquiera exeptuando los negativos y el cero "))
result=number%2

if result == 0:
          print("El numero que escribio es par ", number)
else:
          print("El numero es Impar ", number)

