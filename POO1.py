class Coche():
          largoChasis=250# propiedades de la clase Coche
          anchoChasis=120
          ruedas=4
          enmarcha=False
          
          def arrancar(self):#Metodo arracar, el parametro self python obliga a ponerlo es como poner mi coche.enmarcha
                    self.enmarcha=True
          
          def estado(self):#Metodo estado
                    if miCoche.enmarcha:
                              return "El coche esta en marcha "
                    else:
                              return "El coche esta detenido "

miCoche=Coche()#metodo, Instancia o manda a lamar la clase Coche
print("El largo del chasis es de: ", miCoche.largoChasis)#Imprimer el largo del chasis segun se declaro en la clase
print("El coche tiene ", miCoche.ruedas, "ruedas ")#Imprime cuantas ruedas tiene el coche segun se declaro en la clase
miCoche.arrancar()#Manda a llamar el estado arrancar y esto arranca o inicia el objeto arrancar si no llamo el metodo arrancar 
#el estado del coche seria detenido
print(miCoche.estado())#imprime el estado del coche
