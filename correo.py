#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico 
# con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
correo=input("ingrese su correo electronico ")
print(correo[:correo.find('@')] + '@ceu.es' )


#El print esta mostrando la variable correo la primera posicion encontrando con el metodo find asta el arroba 
# y le concatena el arroba ceu.es