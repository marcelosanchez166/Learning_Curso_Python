#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.


inversion=float(input("ingrese el monto de su inversion "))
interes=float(input("Ingrese el interes anual "))
NAnos=int(input("Escriba el numero de años "))

res=0
for i in range(NAnos):
          i=i+1
          total=inversion*interes*i
          total=total+inversion
          #contador=contador+1
          print("el capital obtenido durante el año ", i,"es ", total )
