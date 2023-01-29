"""Que son las expresiones regulares:"""
# Hay muchas expresiones regulares, son como un mini legunje de programacion dentro de otro lenguaje de programacion
# Son una secuencia de caracteres que forman un patron de busquedas de texto.
# PARA: buscar texto en una base de datos buscar una frase caracter etc,
# Ejmplos: Buscar un texto que se ajusta a un formato determinado (Correo electronico )
# Buscar si existe o no una cadena de caracteres dentro de un texto
# Contar el numero de coincidencias dentro de un texto

"""Buscar en google regular expressions python """

"""sintaxis:"""

"""Ejemplos:"""


import re
cadena = "Vamos a aprender expresiones regulares "

"""Metodo search"""
# re.search Sirve para buscar una palabra en una cadena de texto
# print(re.search("Vamos", cadena))#recibe dos parametros uno la palabra a buscar y dos en donde lo va a buscar

# text="aprender"
# if re.search(text, cadena) is not None:
#           print("He encontrado el texto: {}".format(text))
# else:
#           print("No he encontrado el texto")


# """Metodo start"""  # este metodo mustra la posicion del primer caracter que se busca los espacios en blanco cuentan y
# # comienza a contar desde cero
# text = "aprender"
# textoEncontrado = re.search(text, cadena)
# print(textoEncontrado.start())

# """Metodo end"""  # este metodo mustra la posicion del ultimo caracter que se busca los espacios en blanco cuentan y
# # comienza a contar desde cero
# print(textoEncontrado.end())

# """Metodo span"""  # este metodo mustra las posiciones del primer caracter y del ultimo caracter de la palabra y los muestra en una tupla
# print(textoEncontrado.span())


# """Metodo findall"""
# # Este metodo devuelve una lista con la veces que se encuentra la palabra que se busca
# cadena1 = "Vamos a aprender expresiones regulares en python. python es un lenguaje de sintaxis sencilla "
# textoBuscar = "python"
# print(re.findall(textoBuscar, cadena1))



"""-----------------------Expresiones regulares 2 meta caracteres(caracteres comodin) -------------------"""

"""Meta caracteres
^, $
"""

# #Anclas ^
# import re
# Lista_Nombres=["jose Lopez", "Juan Lopez", "Julio Gutierrez", "Mario Vanegas"]
# Lista_Dominios=["http://holamundo.com", "http://holamundo.es", "ftp://holamundo.com", "ftp://holamundo.es", "https://holamundo.es","http://holamundo.com"]
# Lista_Dominios2=["http://holamundoespañol.com", "http://holamundo.es", "ftp://holamundo.com", "ftp://holamundo.es", "https://holamundo.es","http://holamundo.com"]

# Gente=["Hombres", "Mujeres", "niñas", "niños"]

# for elemento in Lista_Nombres:
#     if re.findall("^jose", elemento):
#         print(elemento) #lo que va a devolver es la coincidencia de jose Lopez porque es el unico que tiene al principio jose

# for element in Lista_Nombres:
#     if re.findall("Lopez$", element):
#         print(element) #lo que va a devolver es la coincidencia de jose Lopez y Juan Lopez porque extra los valores que terminen con el Apellido Lopez

# for dominios in Lista_Dominios:
#     if re.findall("es$", dominios): # "^https"
#         print(dominios) #lo que va a devolver es la coincidencia de los dominios que terminen con .es

# for dominios2 in Lista_Dominios2:
#     if re.findall("[ñ]", dominios2): 
#         print(dominios2) #lo que va a devolver es la coincidencia de algun dominio que contenga la letra ñ en cualquier parte del nombre


# for gentes2 in Gente:
#     if re.findall("niñ[oa]s", gentes2): 
#         print(gentes2) #lo que va a devolver es la coincidencia de los valores que tengan esos caracters que comience con niñ que pueda tener la o ó la a y termine con s



"""-----------------------------------------------------Expresiones regulares 3---------------------------------------------------------"""
#Expresiones regulares con rangos

# import re
# Lista_Nombres=["jose Lopez", "Juan Lopez", "Julio Gutierrez", "Mario Vanegas"]

# for elemento in Lista_Nombres:
#     if re.findall("[o-p]", elemento):
#     #if re.findall("[^O-T]", elemento):Mostrara los valores que tengan mayuscula la y contengan el rango de letras desde la O hasta la T
#     #if re.findall("[o-t$]", elemento):Mostrara los valores que terminen con o con t
#         print (elemento)#Imprimira los valores que dentro de ellos tenga la letra o hasta la t por ejemplo mostraria todos los valores porque tienen la o en cada nombre
#         #Esta funcion distingue entre mayusculas y minusculas



"""-----------------------------------------------------Expresiones regulares 4---------------------------------------------------------"""
#Expresiones regulares con Match y Search

#La funcion match busca coincidencias en un patron de busquedas al comienzo de una cadena de texto

import re 
# name1="Pucas Lopez"
# name2="Luisa Perez"
# name3="Lucas Perez"

# if re.match("Luisa", name2):#re.IGNORECASE= Sirve para que traiga el nombre aunque comience con minuscula o mayuscula
#     #if re.match(".ucas", name2):
#     print("Lo hemos encontrado")
# else:
#     print("No lo hemos encontrado ")


# cadena1="Pucas Lopez"
# cadena2="a3190120432"
# cadena3="42348509"

# if re.match("\d", cadena3):#en esta condicion le pregunto que si la cadena3 comienza con un numero que la muestre
#     print("Lo hemos encontrado")
# else:
#     print("No lo hemos encontrado ")


#Funcion Search Esta Funcion busca en toda la cadena de texto
# name1="Pucas Lopez"
# name2="Luisa Perez"
# name3="Lucas Perez"


# if re.search("Perez", name3):#en esta condicion le pregunto que si la cadena3 comienza con un numero que la muestre
#     print("Lo hemos encontrado")
# else:
#     print("No lo hemos encontrado ")


codigo1="1212121122999230es1212302303434"
codigo2="0009es3934734348739123834348"
codigo3="asdasdasdasdasdljasdlasjññ"


if re.search("es", codigo2):#en esta condicion le pide que busque las letras es en la variable si esta lo muestra 
    print("Lo hemos encontrado")
else:
    print("No lo hemos encontrado ")
