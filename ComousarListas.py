#para el constructor list cuando se manda a llamar debo pasarlo a tupla para que se le pueda pasar mas de un valor
#eje: le pongo doble parentesis para crearlo como tupla
lista1=list((1,2,3))


# Tambien se puede crear una lista a partir de un rango
#eje:
r=list(range(1,10))


#para ver que metodos puedo ejecutar en una lista es la funcion dir
#eje:
listas=["red","blue"]
#print(dir(listas))
#print(dir(listas))

lista=[1,2,3,4,"red","pan", [12, 3, 4, True, "false"]]
#print(lista[0][1])


#Con  el metodo extend se puede agregar mas de un valor a una lista creandolo como tupla algo asi, los elementos se agregan al final
lista.extend([9,10,11,"papas"])
print(lista)
lista.extend((0,20,30,49,"jocotes"))
print(lista)
print(len(lista))

#Metodo para quitar elementos de una lista, si no coloco el indice quita el ultimo valor 
lista.pop()
#mismo metodo pop par aquitar el indice que le indique
lista.pop()


#Tambien se puede remover un valor especifco de una lista con el metodo remove
lista.remove(11)


#Tuplas estas se declaran con parentesis y no pueden cambiar sus valores
#Eje:
x=(1,2,3)
#tambien tiene su constructor y se declara como tuple
#Eje:
y=tuple(("mango", "tom"))

#La diferencia entre una tupla y una lista es que la tupla tiende a ser mas rapida y solo puede ser de un tipo de datos str,int, float,
#ademas dependera del tipo de aplicacion que se este creando ademas que sus valores no cambian
#Para declarar una tupla de un solo elemento debo poner una coma
#Ejem:
e=(1,)


#tipo de datos "set"
#Los metodos set no se pueden acceder mediante indice y se declaran de la siguiente forma
colors={"rede","blue","green"}
#Si quiero agregar un valor al set este sera agregado al inicio del set y lo agrega al inicio porque no tiene un indice


"""#########################################################################################################################"""
#DICCIONARIOS, las claves para los diccionarios van en dobles comillas, Las listas pueden tener dentro varios diccionarios
#Los diccionarios sirven para agrupar valores o caracteristicas de cosas de la vidad real

producto={ "name":'book',
  "cantidad":4,
  "precio":8.99
}
print(producto)

#otro ejemplo
midiccionario={"Italia":"roma",
  "Reino unido":"Londres",
  "España":"Madrid",
  "Alemania":"Berlin"
}
midiccionario["Francia"]="montevideo"# agregar un clave y valor al diccionario
print(midiccionario)
midiccionario["Francia"]="Paris"#modificar el valor de una clave
del midiccionario["Alemania"]#Eliminar una clave y su valor

#Diccionario de distintos tipos claves y valores
dictionari={"Italia":"roma",
  26:"Edad",
  "mosqueteros":3
}


#Diccionario con lista, paso mi lista a un diccionario agregando a cada indice de la lista que se covierte en clave paso un valor
milista=["España","Francia","Reino unido","Alemania"]
midiccionario2={milista[0]:"Madrid",milista[1]:"Paris",milista[2]:"Londres",milista[3]:"Berlin"}
print(midiccionario2)#Mostrar todo el diccionario
print(midiccionario2["Francia"])#Mostar el valor de la clave francia


midiccionario3={23:"Jordan",
          "Nombre":"Michael", 
          "equipo":"Chicago", 
          "Anillos":[1991,1992,1993,1996,1997,1998]
}
print(midiccionario3)#Muestra todo el diccionario
print(midiccionario3[23])#Muestra solo el valor de la clave 23
print(midiccionario3["Anillos"])#Muestra los valores de la clave Anillos (osea todos los años)
print(midiccionario3["Anillos"][2])#Muestra el valor de la posicion 2 para la clave Anillos


#Metodos para usar con los diccionarios
#.keys 
#.values
#len()
print("\n")
print(midiccionario3.keys())#Muestra todas las keys del diccionario
print("\n")
print(midiccionario3.values())#Muestra todos los valores del diccionario
print("\n")
print(len(midiccionario3))#Muestra el tamaño del diccionario




"""############################################################################################################"""

##Funciones 
#Las funciones sirvern para reutilizar codigo por lo que dentro de una funcion puede ir todo el codigo y aparte solo puedo mandarla a llamar
#EJEM:
def hello(name):
  print("Hola Estimado ", name )# aqui no es necesario imprimir la funcion porque arriba imprimo y la funcion solo la llamo y le 
#paso el valor del name

hello("juan")

#Otro ejemplo seria de una suma
def suma(Number1, Number2):
  return Number1+Number2 #Si coloco el return debo mandar a imprimr la funcion 

print(suma(10,40))


"""LIBRERIAS"""

##MODULOS
#Hay 3 tipos de modulos 
#1- Nuestros propios modulos donde podemos escribir nosotros mismos
#2- Modulo que podemos descargar de internet
#3- Modulos de las properia Biblioteca de Python

#Modulos Preconstruidos modulos que nos da python 
#Ejemplo importar fecha y hora
import datetime 
#Para buscar los modulos que hay en python, buscar en google python module
#python datetime
#En pypi puedo buscar modulos o frameworks como (Colorama "init(convert=true)", django, flask, tkinter )

print(datetime.date.day)



#Para mandar a llamar otro archivo .py debo importarlo
#EJEM:
import mifuncion #Nombre del archivo

mifuncion.print_with_exclamation() #Nombre del archivo mas el nombre de la funcion 


print("-", end="")#El edn="" hace que el final de la linea sea nada y escriba lo demas a la par


#Desenpaquetado de tuplas
#Lo que se hace es asignar cada valor de la tupla a una variable y ya python le pasa cada valor en el orden por referencia
#(o en otras palabras por orden de las varibles ) Ej: juan se asigna a nombre y asi sucesivamente
mitupla=("Juan", 12,8,1995)
nombre, dia, mes, year=mitupla
print(year)
print(dia)
print(mes)
print(nombre)