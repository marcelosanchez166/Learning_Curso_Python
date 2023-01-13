#Las funciones ayudan a dividir nuestro programa en fragmentos modulares más pequeños. 
#A medida que nuestro programa crece y se vuelve más complejo, las funciones ayudan a que sea más organizado y manejable.

#Ejercicio funcion len, agregar un valor extra a una lista y contar los valores con la funcion len
letters = ["a", "b", "c"]
letters += ["d"]
print(len(letters))

print("\n")

#ejercicio funcion append, agregar un valor al final de la lista
nums=[1,2,3]
nums.append(4)
print(nums)

print("\n")

#Ejercicio agrega un valor con la funcion index al indice indicado, en este caso en la posicion 0 y corre los demas a la 
# siguiente posicion
Palabras = ['Python', 'diversión']
index = 0
Palabras.insert (index, 'locura')
print(Palabras)

print("\n")

#Ejercicio funcion index, mostrar el indice de un valor de una lista 
letters = ["a", "b", "c"]
print(letters.index('a'))# imprime 0 porque es el indice o posicion del valor a
print(letters.index('b'))# imprime 1 porque es el indice o posicion del valor b


print("\n")
#ejercicio funcion count, puede contar cuántas valores "a" hay en la lista usando: Items.count ("a") donde items es 
# el nombre de nuestra lista.
Items = ["a", "b", "a", "a","c"]
print(Items.count('a'))

print("\n")

#Las cadenas tienen una función format (), que permite incrustar valores en ellas, utilizando marcadores de posición
#Ejemplo:
nums = [4, 5, 6]
Msg = 'Numbers: {0} {1} {2} {2}'. format(nums [0], nums [1], nums [2])#Imprime el orden de la lista en el formato que se la pase
print(Msg)#En esta caso muesta el 4 el 5 y dos veces el 6 por ser la posicion 2 que puse en el .format

print("\n")

#MFuncion .format muestra la posicion 1:abra + posicion 2:cad + posicion 3:abra todo junto es = abracadabra
print("{0}{1}{0}".format("abra", "cad"))

print("\n")

#También puede nombrar los marcadores de posición, en lugar de los números de índice.
#Ejemplo:
A = '{x}, {y} {a}'.format (a= 5, y= 12, x=20)#Muestra los marcadores segun el orden que se le ponga en este mostrara primero 20 12 5 
print(A)

print("\n")


#¡Otra ronda relámpago! Estas son algunas de las otras funciones de cadena útiles:

print(',' .join (['spam', 'huevos', 'jamón'])) #Join: une una lista de cadenas con otra cadena como separador.
#prints 'spam,huevos,jamón'

print('Hola ME'.replace('ME', 'mundo'))#replace : reemplaza una subcadena de una cadena por otra.
#prints 'Hola mundo'

print('Esto es una oración.'.startswith ('Esto'))#Startswith y endswith: determina si hay una subcadena al principio y al final de una cadena, respectivamente.
# imprime 'Verdadero'

print('Esto es una oración.'.endswith ('oración.'))#Startswith y endswith: determina si hay una subcadena al principio y al final de una cadena, respectivamente.
# imprime 'Verdadero'

print('Esto es una oración.'.upper ())#lower  y upper: cambia el caso de una cadena
# imprime 'ESTA ES UNA ORACIÓN'

print('UNA SENTENCIA TODO EN MAYÚSCULAS'.lower ())#lower  y upper: cambia el caso de una cadena
# imprime 'una oración en mayúsculas'r

print('spam, huevos, jamón'.split (','))#Split: lo opuesto a join, convierte una cadena con un determinado separador en una lista.
#prints '['spam', 'huevos', 'jamón']'
