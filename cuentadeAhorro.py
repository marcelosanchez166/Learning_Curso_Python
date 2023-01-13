##Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
#que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
#Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, 
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
#segundo y tercer años. Redondear cada cantidad a dos decimales.

dinero=float(input("Ingrese la cantidad de dinero que desea ahorrar "))

interes=0.04

FirstA = dinero * (1 + interes)
print("Balance tras el primer año:" + str(round(FirstA, 2)))
secondA = FirstA * (1 + interes)
print("Balance tras el segundo año:" + str(round(secondA, 2)))
ThirdA = secondA * (1 + interes)
print("Balance tras el tercer año:" + str(round(ThirdA, 2)))

#sum=0
#interes=0.04
#for i in range(3):
#          resultado = dinero * interes
#          sum = sum + resultado
          #resultado=resultado*dinero
#          print("el saldo total de su cuenta pero el año N° " + str(sum))
#i = i + 1