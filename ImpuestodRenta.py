#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta	                 Tipo impositivo
#Menos de 10000€	          5%
#Entre    10000€ y 20000€	15%
#Entre    20000€ y 35000€	20%
#Entre    35000€ y 60000€	30%
#Más  de  60000€	          45%

salario=float(input("Ingrese su salario mensual "))
renta=""
sueldo=""
if salario<10000:
          renta=salario*0.05
          sueldo=salario-renta
          print("su salario es menor a 10000€ " + "El descuento de la renta por su salario es ", str( renta))
          print("Su salario con el descuento de renta es : ", sueldo )

if salario>=10000 and salario<20000:
          renta=salario*0.15
          sueldo=salario-renta
          print("su salario es mayor  a 10000€ " + "El descuento de la renta por su salario es ", renta)
          print("Su salario con el descuento de renta es : ", sueldo )

if salario>=20000 and salario<35000:
          renta=salario*0.20
          sueldo=salario-renta
          print("su salario es mayor a 20000€ " + "El descuento de la renta por su salario es ", renta)
          print("Su salario con el descuento de renta es : ", sueldo )

if salario>=35000 and salario<60000:
          renta=salario*0.30
          sueldo=salario-renta
          print("su salario es mayor a 35000 " + "El descuento de la renta por su salario es ", renta)
          print("Su salario con el descuento de renta es : ", sueldo )
                              
if salario>=60000:
          renta=salario*0.45
          sueldo=salario-renta
          print("su salario es mayor a 60000 " + "El descuento de la renta por su salario es ", renta)
          print("Su salario con el descuento de renta es : ", sueldo )