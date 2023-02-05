#-------------------------------------------------Que es la documentacion de nuestros programas
"""Incluir comentarios en clases, metodos, modulos etc"""
"""Sirve para ayudar el trabajo en equipo, especialmente en aplicaciones complejas"""


###Tambien se puede colocar documentacion(Comentarios) en las clases 
###Tambien se puede agregar documentacion a los modulos para cuando se importe en otro modulo(archivo) pueda decir para que sirve ese modulo y 
# si el modulo tiene funciones o clases tambien se puede poner documentacion(Comentarios) en ellas

#Ejemplo Documentacion 

# def AreaCuadrado(lado):
#     """Sirve para calcular el area de un cuadrado """
#     return "el area del cuadrado  es: "+str(lado*lado)

# def Areatriangulo(base,altura):
#     return "El area del triangulo es: "+str((base*altura)/2)


# print(AreaCuadrado(3))
# print(AreaCuadrado.__doc__)#Al imprimir la documentacion de  la funcion se muestra el comentario que esta dentro de la funcion 
# help(AreaCuadrado)#De esta manera se imprimira el comentario que esta dento de la funcion 


""" ------------------------------------------Utilizar la documentacion para hacer pruebas de codigo----------------------------"""
#Modulo doctest


# def Areatriangulo(base,altura):
#     ##Para hacer pruebas de que el codigo funciona bien se ponen tres signos de mayor y despues la funcion si la funcion recibira valores se le colocan, 
#     #justo abajo de los signos de mayor se coloca el resultado que se espera obtener de la prueba en la funcion, si no devuelve nada el programa funciona bien, si no devolvera un error, 
#     #pero si lo que la funcion devolvera es un string hay que poner en la prueba todo el string que devolvera hasta con los espacios por ejemplo, 
#     #'El area del triangulo es:  9.0' y el string esperado es con comillas simples
#     #Ademas se pueden relizar varias pruebas en la misma funcion 
#     """
#     Funcion que sirve para calcular la Area de un triangulo 
#     >>> Areatriangulo(3,6)
#     9.0
#     """
#     return (base*altura)/2

# import doctest
# doctest.testmod()


#Ejemplo con pruebas de codigo
# def email(mailuser):
#     """
#     Comprueba que el correo sea un correo valido, Busca un arroba @ en el string no debe estar en el final ni debe tener mas de una arroba @
#     >>> email('marcelosanchez166@gmail.com')
#     True
#     >>> email('@juanlopez.com')
#     False
#     >>> email('lopezlopez.com@')
#     False
#     >>> email('jperez.com')
#     False
#     >>> email('juan@perez@.com')
#     False
#     """
#     arroba=mailuser.count("@")
#     if (arroba !=1 or mailuser.rfind("@")==(len(mailuser)-1) or mailuser.find("@")==0):
#         return False
#     else:
#         return True


# import doctest
# doctest.testmod()

#--------------------------Pruebas de Codigo con doctest para cuando quremos probar un bucle, sentencias anidadas etc

import math 
valores=[]
def raizCuadrada(Listanum):
    """Funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasados por parametros en otra lista
    >>> Lista =[4,9,16]
    >>> Lista2=[]
    >>> for i in Lista:
    ...     Lista2.append(i)
    >>> raizCuadrada(Lista2)
    [2.0, 3.0, 4.0]

    >>> Lista3=[4,-9,16]
    >>> Lista4=[]
    >>> for li in Lista3:
    ...     Lista4.append(li)
    >>> raizCuadrada(Lista4)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """

##Para esta segunda prueba se le pasa el error que esperamos y los tres puntos en medio del error indican que dentro de esas lineas hay mas codigo de error

##Para Anidar expresiones en las pruebas se debe poner tres puntos como en el ejemplo de arriba en el ciclo for
    for nums in Listanum:
        n=math.sqrt(nums)
        valores.append(n)
    return valores

#print(raizCuadrada([9, -16, 25, 36]))
import doctest
doctest.testmod()

#Misma funcion solo que mas corta

# def raizCuadrada(Listanum):
#     """Funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasados por parametros en otra lista
#     """
#     return [math.sqrt(nums)for nums in Listanum]