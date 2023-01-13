#GENERADOR YIELD
#El generador yield sirve para pausar ciertos valores, al llamar la funcion generarpares y pasarle el valor 10
#lo guardo en una variable devuelvepares y esta me mostrara los valores que contiene solo cuando la llame uno a uno y 
# no mostrara la lista completa de numeros pares, Pero solo puedo imprimir los valores exactos no mas, en este caso 9 valores 
# 2, 4, 6, 8 ... etc asta 18

def generarpares(limte):
          num=1
          while num<limte:
                    yield num*2
                    num+=1
devuelvepares=generarpares(10)

print(next(devuelvepares))
print("Aqui podria ir mas coidgo ")

print(next(devuelvepares))
print("Aqui podria ir mas coidgo ")

print(next(devuelvepares))
print("Aqui podria ir mas coidgo ")


#GENERADOR YIELD FROM
#Sirve para imprimir los subelementos del elemento padre para recorrerlos elementos de un generador yield from se hace
#con el bucle for anidado
#EJ:
def devuelve_ciudades(*ciudades):#El asterisco le dice a python que se le pasaran N numero de valores, 
          #osea no sabemos cuanto y los recibe en forma de tuppla
          for elemento in ciudades:#For para recorrer los elementos 
                    for subelemento in elemento:# Este for recorre los valores de cada uno de los alementos, osea los subelementos
                              yield subelemento# en este caso devolveria los subelementos
#Eje: para el primer valor regresaria las letras del primer elemento si las mandamos a imprimr 

ciudades_devueltas=devuelve_ciudades("santa ana", "apopa", "san salvador", "mexicanos")
print(next(ciudades_devueltas))


##YIELD from
def devuelve_ciudades(*ciudades):#El asterisco le dice a python que se le pasaran N numero de valores, 
          #osea no sabemos cuanto y los recibe en forma de tuppla
          for elemento in ciudades:#For para recorrer los elementos 
                              yield from elemento# en este caso devolveria los subvalores del cada valor de la variable elemento
#Eje: para el primer valor regresaria las letras del primer elemento si las mandamos a imprimr 

ciudades_devueltas=devuelve_ciudades("santa ana", "apopa", "san salvador", "mexicanos")
print(next(ciudades_devueltas))

