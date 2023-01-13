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

class moto(vehiculos):#Forma para heredar de la clase padre en este caso de clase vehiculos
          pass

mimoto=moto("honda ", "Navi ")#Instancias la clase moto con lo que hereda de clase vehiculos
mimoto.arrancar("Avanzando")#pasar parametro al metodo arrancar
mimoto.estado()#Mostrar el estado



"""Sobre escritura de Metodos y Herencia simple y Multiple"""

#La Sobre escritura de Metodos se da cuando mandamos a llamar o creamos un metodo de una clase dentro de la clase padre por ejemplo
#Para la clase moto llamaremos el metodo estado sobreescribiendo el metodo ESTADO

class moto(vehiculos):#Forma para heredar de la clase padre en este caso de clase vehiculos
          hcaballito=""
          def caballito(self):#Metodo caracteristicos de las motos y bicicletas
                    self.hcaballito="Voy haciendo el caballito" 
          def estado(self):#Seobre escritura de metodos se copia el metodo de la clase padre
                    print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEl vehiculo esta:  ", self.enmarcha, 
                    "\nAcelerando: ", self.acelera, "\nfrenando: ", self.frena, "\n", self.hcaballito)#En este print se llaman las variables
                    # de las propiedades de la clase que estan dentro del constructor


mimoto=moto("honda ", "Navi ")#Instancias la clase moto con lo que hereda de clase vehiculos
mimoto.arrancar("Avanzando")#pasar parametro al metodo arrancar
mimoto.estado()#Mostrar el estado


"""En la Herencia Multiple sle da preferencia a la primera clase que se le indique a la clase que indique primero 
en la clase hijo o que hereda"""


class VElectricos():#Esta clase no esta heredando de ninguna otra clase
          def __init__(self):#Contructor propio de la clase VElectricos
                    self.autonomia=100
          def cargarEnergia(self):#Metodo propio de la clase cargarEnergia 
                    self.cargando=True
          


class BiciElectrica(VElectricos,vehiculos):#se da preferencia a la primera clase que se le indique
          pass

mibici=BiciElectrica()#Instancio la clase BiciElectrica, por eso en este caso no se le pasa ningun argumento a la instanciacion de la clase 
#porque el toma el constructor de la clase VElectricos y ese constructor solo tiene el argumento por defecto "self"


