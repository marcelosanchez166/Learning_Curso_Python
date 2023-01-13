##Peso (kg) / altura (m)2
#165 cm (1,65 m)     
#68 kg
peso=float(input("ingrese su peso en kilogramos "))
altura=float(input("Ingrese su estatura en metros "))
IMC=peso/altura**2
print("su IMC ideal es de " + str("{0:.3f}".format(IMC)))
##con la funcion "{0:.3f}".format(IMC) estoy redondeando el resultado a imprimir de la variable IMC
## se puede poner cuantos decimales quieron al cambiar "{0:.3f}"