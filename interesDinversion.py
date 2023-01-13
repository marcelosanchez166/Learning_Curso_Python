inversion=float(input("Ingrese el monto a invertir "))
Interes=float(input("Ingrese el interes de acuerdo al monto "))
Nanos=float(input("Escriba para cuantos años es la inversion "))
dias=Nanos*365 ##conversion de años a dias
TSinteres=(inversion * Interes * 30 ) / dias
print("su inversion le genero la siguiente tasa de interes " + str("{0:.2f}".format(TSinteres)))
