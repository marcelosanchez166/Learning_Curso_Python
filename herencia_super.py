class vehiculos():
          def __init__(self, marca, modelo):#Constructor, recibe dos parametros que tienen en comun todos los vehiculos
                    self.marca=marca#Carasteristicas de todo tipo de vehiculo
                    self.modelo=modelo#Carasteristicas de todo tipo de vehiculo
                    self.enmarcha="Detenido"#Carasteristicas de todo tipo de vehiculo
                    self.acelera="No"#Carasteristicas de todo tipo de vehiculo
                    self.frena="NO"#Carasteristicas de todo tipo de vehiculo
          
          def arrancar(self, marcha):#Metodos de todo tipo de vehiculo
                    self.enmarcha=marcha
                    if self.enmarcha==marcha:
                              print()
                    else:
                              print("La moto esta detenida")

          def acelera(self):#Metodos (o cosas que hacen) de los tipo de vehiculo
                    self.acelera="si"

          def frenar(self):#Metodos de todo tipo de vehiculo
                    self.frena="si"

          def estado(self):
                    print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEl vehiculo esta:  ", self.enmarcha, 
                    "\nAcelerando: ", self.acelera, "\nfrenando: ", self.frena)


"""Funcion Super para las clases"""

#La funcion super manda a llamar el metodo(Constructor) que en este caso recibe dos parametros ademas del self de la clase padre, 
#que se le pase a la clase en este caso de la clase Vehiculos


class VElectricos(vehiculos):#Esta clase esta heredando de la clase vehiculos
          def __init__(self,marca, modelo ):#Contructor propio de la clase VElectricos

                    super().__init__(marca, modelo)#Con la funcion super manda a llamar el metodo(Constructor) de la clase 

                    self.autonomia=autonomia
          def cargarEnergia(self):#Metodo propio de la clase cargarEnergia 
                    self.cargando=cargando
          


class BiciElectrica(VElectricos,vehiculos):#se da preferencia a la primera clase que se le indique
          """Si defino un constructor para la clase BiciElectrica tengo que pasarle los valores del contrutor de la clase padre
          Eje"""
          def __init__(self, tipo, ring, marca, modelo  ):#Constructor de la clase bici
                    #Le debo pasar los demas valores que recibe la clase padre vehiculos

                    super().__init__(marca, modelo)#Con la funcion super manda a llamar el metodo(Constructor) de la clase 
                    #padre vehiculos, con los valores que necesita

                    super().cargarEnergia()#Con la funcion super manda a llamar el metodo de la clase vehiculos

                    self.tipo=tipo#CARACTERISTICAS DE UNA BICICLETA#
                    self.ring=ring#CARACTERISTICAS DE UNA BICICLETA#


                    
          def estado(self):#Mando a llamar el metodo estado de la clase vehiculos se debe hacer con el mismo nombre
                    super().estado()#Con la funcion super mando a llamar el metodo estado de la clase padre vehiculos
                    print("tipo de bicicleta: ",self.tipo, "\nTamaño del ring: ", self.ring, "\nAutonomia: ",self.autonomia, 
                    "\nCargando vehiculo:",self.cargando )

autonomia=input("ingrese la autonomia actual del auto: ")
cargando=input("El auto esta cargando SI/NO: ")

mibici=BiciElectrica("Corsario", "hj310i" , "BMX", "Ring 26'" )#Intanciacion de la clase BiciElectrica
mibici.estado()


#En python se tiene una funcion """isinstance()""" que nos informa si un objeto es instancia de una clase cualquiera devuelve true o false
"""Eje"""
#print(isinstance(mibici,VElectricos))



