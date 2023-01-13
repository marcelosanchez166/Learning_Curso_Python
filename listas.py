#Creamos 2 listas vacias
lista1 = []
lista2 = []

#Preguntamos al usuario cuantos datos desea integrar
cantidad = int(input("Cuantos datos desea agregar: "))

#Greneramos un cilo para que se repitan las preguntas mientras la cantidad sea mayor que 0
while cantidad>0:
          #Pedimos que indique en que lista deea guardar su dato
          lista = input("En que lista desea ingresas sus datos \n1) Lista1 \n2) Lista2 \n")
          #Pedimos el dato
          dato = input("Ingrese sus datos: ")
          #Comprobamos la decision del usuario para saber en que lista se guardara el dato
          if lista == 1:
                    lista1.append(str(dato))
          else:
                    lista2.append(str(dato))
          #Quitamos de a uno en uno los intentos de el valor inicial que l usuario indico para poder detener el ciclo
                    cantidad-=1
#Finalmente imprimimos el contenido de las listas
print("Contenido lista1:\n",lista1)     


