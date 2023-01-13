##Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
#Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y
#el coste final total.

descuento=0.60
Cbarras=3.49

barrasV=float(input("Escriba la cantidad de barras que vendio de no son del dia "))
costo=Cbarras*barrasV
desc=costo*descuento
print("El costo normal de una barra es de ", Cbarras)
print("El descunto por barra ya que no son del dia es del ", descuento, "Descuento total de su compra", desc )
Ftotal=costo-desc
print("El total por las barras es de ", "{0:.2f}".format (Ftotal ))