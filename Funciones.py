#Funciones

Numero=int(input("ingresé un número para la tabla de multiplicar:  "))

def mostrar_linea(num, línea):
      print (num,"x",línea,"=",num * línea)

for i in range(11):
      mostrar_linea(Numero,i)     

#A la funcion mostrar_linea se le pasan las variables Numero e i, ya que espera dos valores, Numero remplaza a num e i remplaza a linea
#En el ciclo for