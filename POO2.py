class Coche():
          largoChasis=250# propiedades de la clase Coche
          anchoChasis=120
          ruedas=4
          enmarcha=False
          
          def arrancar(self,arrancamos):#Metodo arracar, el parametro self python obliga a ponerlo, le pasamos el parametro arrancamos 
                    if self.enmarcha==arrancamos:
                              return "El coche esta en marcha "
                    else:
                              return "El coche esta detenido "
          
          def estado(self):#Metodo estado
                    print("El coche tiene ", self.ruedas, "ruedas ", "el largo del choche es ", self.largoChasis, "el ancho es de ", 
                    self.anchoChasis, "ancho")


miCoche=Coche()#metodo, Instancia o manda a lamar la clase Coche
print(miCoche.arrancar(True))#Manda a llamar el estado arrancar y esto arranca o inicia el objeto arrancar si no le paso un valor true o false 
#error
miCoche.estado()#llama el metodo estado

print("----------------El programa continua---------------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()


#Para especificar un estado inicial de las propiedades de una clase se da con un constructor, el constructor da estado incial 
#a las propiedades, para que cuando se cree la instanciacion de la clase (objeto) ya tengan las caracteristicas de la clase osea 
#sus propiedades y para eso hay que meterlas en un contructor

#Para crear un constructor es de la siguiente forma, el constructor siempre tiene el nombre __init__
#Se necesita que las propiedades vayan presedidas por el parametro self para que formen al estado inicial
def __init__(self):
          self.largoChasis=250# propiedades de la clase Coche
          self.anchoChasis=120
          self.ruedas=4
          self.enmarcha=False
#con esto le digo a python que este es el constructor de la clase y es quien va a dar estado incial a las 
#propiedades que pertenecen a la clase


#######################################################################
#Para evitar la modificacion de las variables de propiedades de la clase se utiliza el encapsulamiento
#Para encapsular una propiedad en python hay que poner el nombre de la variblle con dos guiones bajos, 
"""self.__ruedas"""
#y cada ves que se utilice esa variable hay que usarla de la misma forma con los guiones