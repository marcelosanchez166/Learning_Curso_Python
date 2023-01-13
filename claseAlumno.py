class Alumno:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del alumno")
        self.Edad = int(input("Edad del alumno"))

    def imprimir(self):
        print("Alumno: ", self.nombre)
        print("Edad: ", self.Edad)

    def Resultado(self):
        if self.Edad < 18:
            print("El alumno es menor de edad ")
        else:
            print("Alumno mayor de edad")


Alumno1 = Alumno()
Alumno1.imprimir()
Alumno1.Resultado()
