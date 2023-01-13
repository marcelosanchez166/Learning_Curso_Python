#Lambda son funciones anonimas, Consiste en resumir una funcion normal, no todo lo que se puede hacer con una funcion normal se 
#puede hacer en una funcion lambda, No siempre se puede usar funciones lambda, Se usa mas que todo para Funciones sencillas, 
#las funciones con bucles, condicionales no se pueden convertir en funciones lambda

#Ejemplo: Realizar repetidamente el calculo del Area de un triangulo

#Funcion normal
# def area_traigulo(base,altura):
#     return(base*altura)/2

# print(area_traigulo(5,7))

#Funcion Lambda
#Se crea una variable area_triangulo, se pone la funcion lambda y se ponen los parametros que va a recibir, luego se ponen dos puntos que 
#es como poner return y luego se le pone lo que quiero que haga

#Las funciones Lambda son tambien conocidas como 
#On the go
#On demand
#Online
area_traigulo=lambda base, altura:(base*altura)/2
print(area_traigulo(7,5))


#Lambda Al cubo, Se puede hacer de dos formas con la funcion pow que requiere dos parametros
#pow(numero, 3)
al_cubo=lambda numero:numero**3

print(al_cubo(13))


destacar_valor=lambda comision: "¡{}! $ ".format(comision)

print(destacar_valor(34))

comision_luis=1555
print(destacar_valor(comision_luis))