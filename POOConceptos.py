"""VOCABULARIO DE POO"""
#clase
#Objetos
#instancia de clase, instanciar una clase
#programas divididos en trozos= modularizacion (modulos)
#atributos
#encapsulamiento 
#herencia = se refiere a que el codigo es reutilizable
#polimorfismo


#Herencia
#La herencia permite que se puedan definir nuevas clases basadas de unas ya existentes a fin de reutilizar el código
#generando así una jerarquía de clases dentro de una aplicacion
#Sirver para Si una clase deriva de otra, esta hereda sus atributos y métodos y puede añadir nuevos atributos, métodos o redefinir los heredados.


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