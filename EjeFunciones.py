#Ejercicio 1
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
# def saludo():
#           print("Hola amiga")
# saludo()
# saludo()
"""###########################################################################################################"""

#Ejercicio 2
#Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.
# def msj(name):
#           print("¡hola! " ,name)
# name="Marcelo"
# msj(name)

"""############################################################################################################"""

#Ejercicio 3
#Escribir una función que reciba un número entero positivo y devuelva su factorial.

# def numero(num):
#           if num==1 or num==0:
#                     return 1
#                     #usando recursión en Python, La recursión es llamar a la misma función una y otra vez 
#           else:
#                     return num *numero(num - 1)# n va tomado el valor ya multiplicado, y numero(num-1)le resta 1 al valor de n desde que entra
#                     #en ejecucion el codigo del if

# num=int(input("Ingrese un numero entero positivo "))
# numero(num)
# print("Factorial of",num,"is", numero(num))
"""############################################################################################################"""

#Ejercicio 4
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe 
#recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
#Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

# def factura(subtotal, iva):
#           if iva==0 :
#                     total=subtotal*0.21
#                     total2=subtotal+total
#                     print(total2)
#           else:
#                     total=subtotal*iva
#                     total2=subtotal+total
#                     print(total2)
# sub=float(input("Ingrese el monto de la factura: "))
# impuestoIVA=float(input("Ingrese el porcentaje de iva a aplicar: "))
# factura(sub, impuestoIVA)

"""Otra forma de hacerlo"""

# def invoice(amount, vat=21):
#           return amount + amount*vat/100

# print(invoice(1000,10))#En esta se le pasa el parametro del iva
# print(invoice(1000))#En esta no se pasa el valor al iva 
"""####################################################################################################################"""

#Ejercicio 5
#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

# def area_circulo(radio):
#           pi=3.14
#           return pi*(radio**2)
# print(area_circulo(3))

# def area_cilindro(radio, high):
#           return area_circulo(radio)*high#Usa el valor de radio del area de la primera funcion are_circulo para calcular el area del cilindro
# print(area_cilindro(3,5))#Imprime el area del cilindro


"""##################################################################################################################"""

#Ejercicio 6
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.


# def muestra(lista):
#           media=0
#           for i in lista:#Cuando se hace esto el valor que tomara i sera cada indice de la lista en este caso primero sera 1 luego 2 etc
#                     print(i)#imprime el primer indice que toma i de la lista 
#                     media=media +i#Suma y guarda cada valor de la lista, primero toma el valor 1 y lo guarda en media luego media vale 1
#                     #e i vale 2 lo suma y ahora media vale 3 y asi sucesivamente
#                     media2=media/len(lista)#Se gurda la division de la suma de todos los valores de la lista y se divide entre el tamaño de
#                     #la lista
#           print(media2)#Imprime la media

# lista=[1,2,3,6,79,5,5,6]
# muestra(lista)#Manda a llamar la funcion

"""###################################################################################################################"""
#Ejercicio 7
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

# def muestra_numeros(muestra):
#           list = []
#           for i in muestra:
#                     list.append(i**2)
#           return list
# muestra=[1,2,3,6,79,5,5,6]
# print(muestra_numeros(muestra))

"""##################################################################################################################"""

#Ejercicio 8
#Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

# from math import sqrt

# def muestra_numeros(muestra):
#           list = []
#           diccionario={}
#           media=0
#           for i in muestra:
#                     list.append(i)
#                     media=media +i
#                     media2=media/len(list)
#                     varianza=((i-media2)**2)/len(muestra)-1
#           desviacion_tipica=sqrt(varianza)
#           diccionario={"media":media2, "varianza":varianza, "desviacion_tipica":desviacion_tipica}
#           print(diccionario)
#           return list
# muestra=[1,2,3,6,79,5,5,6]
# print(muestra_numeros(muestra))

"""########################################################################################################################"""
#Ejercicio 9
#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

# def MCD(x, y):
#           maximoCD=1
#           if x % y == 0:
#                     return y
#           for i in range((y/2), 0, -1):
#                     if x % i==0 and y % i==0:
#                               maximoCD=i
#                               break
#           return maximoCD

# def MinimoCM(x, y):
#           z=max(x,y)
#           while True:
#                     if z % x==0 and z % y==0:
#                               return z
#                     z+=1
# print(MCD(8,4))


"""################################################################################################################################"""
#Ejercicio 10
#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

# def Adecimal(n):
#           n=list(n)#Convierte la cadena de texto que se le pasa mediante n, en una lista quedaria n=[1,0,1,1,0]
#           n.reverse()#para convertir un numero binario a decimal se le da vuelta al numero binario en este le da vuelta a la lista
#           #print(n)
#           decimal = 0
#           for i in range(len(n)):#recorre con el for el tamaño de la lista 
#                     #print(i)#impreme el valorque va tomando i al recorrer la lista
#                     decimal += int(n[i]) * 2 ** i#le suma el indice actual de la lista a la variable decimal y luego lo multiplica * 2
#                     #y lo eleva con el valor del indice que tendria actualmemte i
#                     #print(n[i])#Imprime en cada iteracion del indice de la lista recorrida por el ciclo for
#           return decimal


# def Abinario(num):
#           lista=[]
#           while num > 0:
#                     lista.append(str(num % 2))#Saca el residuo de la division entre 2 por cada iteracion asta que num sea menor que cero
#                     #y luego lo convierte a string y lo agrega a la lista 
#                     #print(lista)
#                     num //= 2#hace una Division entera saca solo el entero no pone punto decimal, sino lo pongo se convierte un bucle 
#                     #infinito porque num nunca llega a ser menor que cero
#                     #print(num)
#           lista.reverse()#Invierte los valores de la lista de atras para adelante
#           return ''.join(lista)#Sirve para convertir la lista en una cadena de texto se utiliza la funcion "".join
#           #si se le pone algo entre los parentesis eso lo tomara como separador de cada valor de la lista 

# print(Adecimal('10110'))
# print(Abinario(22))

"""##################################################################################################################################"""

#Ejercicio 11
#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia. 
#Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y 
#su frecuencia.


def funcion(cadena):
          variable=cadena.split()
          diccionario={}
          for i in variable:
                    if i in diccionario:#Itera cada posicion de la cadena y evalua si esta en el diccionario, si esta en el diccionario
                    # le suma 1 al valor de diccionario[i] y si no solo lo agrega que es lo que hace en el else
                              diccionario[i]+=1
                    else:
                              diccionario[i]=1
          return diccionario

def wordrepetida(diccionario):#Llama el diccionario y se lo pasa como parametro a la funcion 
          max_word = ''
          max_freq = 0
          for word, freq in diccionario.items():
                    if freq > max_freq:
                              max_word = word
                              max_freq = freq
          return max_word, max_freq

variable="hola mundo como esta el mundo"
print(funcion(variable))
print(wordrepetida(funcion(variable)))




