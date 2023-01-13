class Coche():
          def __init__(self):#Constructor su nombre es por defecto
                    self.__largoChasis=250# propiedades de la clase Coche
                    self.__anchoChasis=120#Se les pasa el nombre del parametro del contructor (self)
                    self.__ruedas=4#Se ponen dos guiones bajos para encapsulacion  de las variables __0
                    self.__enmarcha=False
          
          def arrancar(self,arrancamos):#Metodo arracar, el parametro elf python obliga a ponerlo, le pasarmos el parametro arrancamos 
                    self.__enmarcha=arrancamos
                    
                    if self.__enmarcha==arrancamos:
                              chequeo=self.__chequeo_interno()

                    if self.__enmarcha==True and chequeo==True:
                              return "El coche esta en marcha "

                    elif self.__enmarcha==True and chequeo==False:
                              return "Algo salio mal en el chequeo "

                    else:
                              return "El coche esta detenido "
          
          def estado(self):#Metodo estado
                    print("El coche tiene ", self.__ruedas, "ruedas ", "el largo del choche es ", self.__largoChasis, "el ancho es de ", 
                    self.__anchoChasis, "ancho")
                    
          def __chequeo_interno(self):##Encapsulando el metodo
                    print("Realizando chequeo interno ") 
                    self.luces="ok"
                    self.puertas="cerradas"
                    self.gasolina="ok"

                    if self.luces=="mal" and self.puertas=="cerradas" and self.gasolina:
                              return True
                    else:
                              return False



miCoche=Coche()#metodo, Instancia o manda a lamar la clase Coche
print(miCoche.arrancar(True))#Manda a llamar el estado arrancar y esto arranca o inicia el objeto arrancar si no le paso un valor true o false 
#error
miCoche.estado()#llama el metodo estado

print("----------------El programa continua---------------------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()