#Pedir numeros al usuario asta que ingrese un numero negativo y luego mostrar la cantidad de numeros introducidos sin contar el negativo

numero=0
contador=-1
while numero>=0:
          numero=int(input("Ingrese un numero por favor "))
          #otra forma de no contar el numero negativo seria 
          #if numero>=0: que sume solo si el numero es mayor o igual a cero
          contador=contador+1
          #otra opcion seria de esta manera para no contar el numero negativo
          #contador=contador - 1
print("La cantidad de numeros que ingreso son ", contador , "numeros")
