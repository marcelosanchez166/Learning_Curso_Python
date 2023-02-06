# Polimorfismo viene del griego poli=Muchas y morfismo=formas

class coche():
    def desplazamiento(self):
        print("Me desplazo en 4 ruedas ")


class moto():
    def desplazamiento(self):
        print("ME desplazo usando 2 ruedas")


class camion():
    def desplazamiento(self):
        print("Me desplazo usando 8 ruedas ")

# Creo una funcion para hacer polimorfismo y asi el parametro vehiculo.desplazamiento obtenga la instancia de la clase que se instancio


# Se guarda la instancia de la clase que se paso a la funcion
def desplazamientoVehiculo(vehiculo):
    # manda a llamar el metodo de la clase que se instancio y se paso
    vehiculo.desplazamiento()


mivehiculo = coche()  # Instanciacion de clase
# Se le pasa el nombre de la instancia para que el le pase a la funcion desplazamientoVehiculo
desplazamientoVehiculo(mivehiculo)

"""otro ejemplo seria instanciar la clase camion"""
mivehiculo = camion()  # Instancio la clase camion
# En la funcion llamaria el metodo desplazamiento de la clase camion
desplazamientoVehiculo(mivehiculo)

mivehiculo=moto()
desplazamientoVehiculo(mivehiculo)