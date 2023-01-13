class Tarjeta:
          def __init__(self, id, cantidad = 0):    # Inicializador
                    self.id = id                         # Creación del atributo id  
                    self.saldo = cantidad                # Creación del atributo saldo
                    return
          def mostrar_saldo(self):
                    print('El saldo es', self.saldo, '€')
                    return
t = Tarjeta('1111111111', 1000)     # Creación de un objeto con argumentos             
t.mostrar_saldo()

