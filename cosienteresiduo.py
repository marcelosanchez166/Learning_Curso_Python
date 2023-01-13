n1=float(input("Ingrese un numero entero "))
n2=float(input("Ingrese otro numero entero "))
cociente=n1//n2
residuo=n1%n2
print("El Cociente de la division es " + str("{0:.2f}".format(residuo)))
print("El Residuo de la division es " + str("{0:.2f}".format(cociente)))

##otro ejemplo mas pro seria 
#minutos, segundos_sobrantes = divmod(segundos, 60)
#print("Minutos: {}, segundos: {}".format(minutos, segundos_sobrantes))