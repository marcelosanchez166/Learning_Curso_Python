"""Que son las expresiones regulares:"""
#Hay muchas expresiones regulares, son como un mini legunje de programacion dentro de otro lenguaje de programacion 
#Son una secuencia de caracteres que forman un patron de busquedas de texto.
#PARA: buscar texto en una base de datos buscar una frase caracter etc, 
#Ejmplos: Buscar un texto que se ajusta a un formato determinado (Correo electronico )
#Buscar si existe o no una cadena de caracteres dentro de un texto
#Contar el numero de coincidencias dentro de un texto

"""Buscar en google regular expressions python """

"""sintaxis:"""
import re

"""Ejemplos:"""




cadena="Vamos a aprender expresiones regulares "

"""Metodo search"""
#re.search Sirve para buscar una palabra en una cadena de texto
#print(re.search("Vamos", cadena))#recibe dos parametros uno la palabra a buscar y dos en donde lo va a buscar

# text="aprender"
# if re.search(text, cadena) is not None:
#           print("He encontrado el texto: {}".format(text))
# else:
#           print("No he encontrado el texto")


"""Metodo start"""# este metodo mustra la posicion del primer caracter que se busca los espacios en blanco cuentan y 
#comienza a contar desde cero
text="aprender"
textoEncontrado=re.search(text,cadena)
print(textoEncontrado.start())
          
"""Metodo end""" # este metodo mustra la posicion del ultimo caracter que se busca los espacios en blanco cuentan y 
#comienza a contar desde cero
print(textoEncontrado.end())

"""Metodo span""" # este metodo mustra las posiciones del primer caracter y del ultimo caracter de la palabra y los muestra en una tupla
print(textoEncontrado.span())



"""Metodo findall"""
#Este metodo devuelve una lista con la veces que se encuentra la palabra que se busca
cadena1="Vamos a aprender expresiones regulares en python. python es un lenguaje de sintaxis sencilla "
textoBuscar="python"
print(re.findall(textoBuscar, cadena1))