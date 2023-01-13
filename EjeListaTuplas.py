#Ejercicio 3
#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
#pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
#has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas 
#introducidas por el usuario.

#3
# asignaturas=["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje", "Informatica"]
# print("Asignaturas del alumno: ")
# print("Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje", "Informatica")
# notas=[]
# def asignatura():
#           i=0
#           while  i < len(asignaturas):
#                     nota=int(input("ingrese la nota para la asignatura "+ str(asignaturas[i]) +": "))
#                     print("\n")
#                     if nota > 10 or nota< 0:
#                               print("La Calificacion que ingresaste es invalida \n")
#                     else:
#                               notas.append(nota)
#                     i=i+1
#           for n in range(len(asignaturas)):
#                     print("En ", asignaturas[n], "Has obtenido ", notas[n])
# asignatura()

"""----------------------------------------------------------------------------------------------------------------------------------"""

#4
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
#los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
# numeros=[]

# for i in range(5):
#           num=int(input("Ingrese el numero " + str(i+1) + " De su billete de loteria: " ))
#           numeros.append(num)
#           numeros.sort()

# #           # menor=i
# #           # for j in range(i+1, 5):
# #           #           if numeros[j] < numeros[menor]:
# #           #                     menor=j
# #           # temporal=numeros[menor]
# #           # numeros[menor]=numeros[i]
# #           # numeros[i]=temporal
# print(numeros)


"""----------------------------------------------------------------------------------------------------------------------------------"""

#5
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
# num=[]
# for i in range(1,11):
#           num.append(i)
# print(num[::-1])


"""----------------------------------------------------------------------------------------------------------------------------------"""

#Ejercicio 6
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
#Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y 
#elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el 
#usuario tiene que repetir.
# asignaturas=["Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje", "Informatica"]
# print("Asignaturas del alumno: ")
# print("Matematicas", "Fisica", "Quimica", "Historia", "Lenguaje", "Informatica")
# notas=[]
# notasmenores=[]

# def asignatura():
#           i=0
#           while  i < len(asignaturas):
#                     nota=int(input("ingrese la nota para la asignatura "+ str(asignaturas[i]) +": "))
#                     print("\n")
#                     if nota > 10 or nota< 0:
#                               print("La Calificacion que ingresaste es invalida \n")
#                     else:
#                               notas.append(nota)
#                     i=i+1
#           for n in range(len(asignaturas)):
#                     if notas[n]<6:
#                               print("Debes repetir la siguiente materia, En la que obtuviste nota menor a 6 ")
#                               print("En ", asignaturas[n], "Has obtenido ", notas[n])
# asignatura()

"""----------------------------------------------------------------------------------------------------------------------------------"""

#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
#y muestre por pantalla la lista resultante.
# abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# for i in range(len(abecedario),1,-1):
#           if i%3==0:
#                     abecedario.pop(i-1)
# print(abecedario)


#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y 
#muestre por pantalla el menor y el mayor de los precios.
"""Se aplico algoritmo de ordenamiento por seleccion"""
# precios=[50, 75, 46, 22, 80, 65, 8]
# for i in range(len(precios)):#Se recorre el tamaño de la lista y se guarda la ultima posicion que en este caso es 6 en la variable minimo
#           minimo=i
#           #print(minimo)
#           for j in range(i,len(precios)):#recorre el vector j y se evalua si la posicion del indice j es menor que que el valor de la 
#                     #posicion de la variable minimo de la lista, si el valor es menor minimo pasa a tener el valor de j
#                     if precios[j]<precios[minimo]:
#                               minimo=j
#           if minimo!=i:#se evalua si el valor del indice i es diferente al valor de la variable minimo
#                     num=precios[i]#Se guarda el valor de la posicion de i para la lista en la varible num
#                     precios[i]=precios[minimo]#Si es diferente intercambian valores, en precios i se guarda el valor de precios
#                     #minimo
#                     precios[minimo]=num#y en precios minimo, se guarda el valor que tiene num
# print (precios)
#print(minimo)

#Ejercicio 13
#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y 
#muestre por pantalla su media y desviación típica.

lista=[]
num=int(input("Cuantos numeros desea ingresar para calcular la deviacion tipica y la media aritmetica: "))
for i in range(num):
          numero=int(input("Ingrese el numero "))
          lista.append(numero)
          mediaA=sum(lista)/len(lista)
          deviacionTi=0
          for i in lista:
                    deviacionTi += i**2
          res = (deviacionTi/len(lista)-mediaA**2)**(1/2)
print(mediaA)
print(res)
print(lista)
