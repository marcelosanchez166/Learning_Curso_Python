#La funcion filter es una de las que se les denomina funciones de orden superior
#Nos permiten utilizar un paradigma de programacion que se denomina programacion funcional

#La funcion hace que verfica que los elementos de una secuencia cumplan una condicion, devolviendo un iterador con los elementos
#que cumplen dicha condicion

# Funcion para detectar que numeros son pares o impares
# def num_par(num):
#     if num%2 ==0:
#         return True
#     else:
#         return False

# listanumbers=[23,4,44,21,55,78]

# print(list(filter(num_par,listanumbers)))


#Tambien se podria usar una funcion lambda en lugar de una funcion normal y obtendremos el mismo resulta que el codigo de arriba
#por ejemplo

# listanumbers=[23,4,44,21,55,78]

# print(list(filter(lambda number: number%2==0,listanumbers)))


#La funcion filter se usa para filtrar objetos

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
    
    def __str__(self):
        return "{} Que trabaja como {} tiene un salario de {} $".format(self.nombre, self.cargo, self.salario)

Listempleados=[ Empleado("Juan", "Director", 1500),
Empleado("Hector", "Bodeguero", 600),
Empleado("Luisa", "Secretaria", 700),
Empleado("Chris", "Tecnico", 900),
Empleado("luis", "Adm DB", 1200)
]

Salarios_altos=filter(lambda employe: employe.salario > 700, Listempleados)

for empleado_salario in Salarios_altos:    
    print(empleado_salario)