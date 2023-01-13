# Un ejemplo de caso de uso de continue:
# Un sistema de emisión de billetes de avión necesita calcular el costo total de todos los billetes comprados.
# Las entradas para niños menores de 3 años son gratuitas.
# Podemos usar un ciclo while para recorrer la lista de pasajeros y calcular el costo total de sus boletos. Aquí,
# la instrucción continue se puede usar para omitir a los niños.


Cpasajeros = int(input("Ingrese la cantidad de pasajeros: "))
print("\n")
Pnombres = []
Pedad = []
name = ""
edad = ""
CostoBoleto = 200
mayores = 0


def pasajeros():
    i = 0
    while i < Cpasajeros:
        name = input("Ingrese el nombre del pasajero:  ")
        Pnombres.append(name)
        edad = int(input("Ingrese la edad del pasajero:  "))

        print("\n")
        i += 1
        if edad >= 3:
            Pedad.append(edad)
            conteo = len(Pedad)
            total = CostoBoleto*conteo
        if edad < 3:

            continue
            # Pedad.append(edad)
    print("El consto total de los billetes de avion para los pasajeros mayores a 3 años es: ", total)


pasajeros()
print("Los nombres de los pasajeros son ", Pnombres)
print(" Edad de los pasajeros mayores a 3 años ", Pedad)
# print(total1)
