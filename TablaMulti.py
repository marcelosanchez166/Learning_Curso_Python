#Pedir un numero por teclado y mostrar los 10 primero terminos de su tabla de multiplicar

numero=int(input("Ingrese un numero "))
contador=0
for i in range(0,10):
          contador=contador+1
          res=numero*contador
          print(numero, "*", contador, "=", res )

##otra forma de hacerlo mas facil seria 
# for i in range (1, 11):
          #print(numero, "*", i, "=", (numero*i))