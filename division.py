#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
#Si el divisor es cero el programa debe mostrar un error.
N1=float(input("ingrese un numero "))
N2=float(input("Ingrese otro numero "))
resul=N1/N2
if N2  == 0:
          print("Ha ocurrido un error ")
else:
          print(resul)
#<