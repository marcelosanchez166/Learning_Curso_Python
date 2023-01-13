
# Convertir celcius a Fahrenheit con la funcion que cree convertir
# Lo que el usuario ingresa y se guarda en celcius se pasa al parametro "c" de la funcion  y hace el procedimiento con el return
# regresa el resultado
# fuera de la funcion impreme el resultado imprimiendo la funcion convertir mas el parametro celcius

"""EL MISMO EJERCICIO 3 VECES"""

celsius = int(input())


def convertir(c):
    return(c * 1.8) + 32


print(convertir(celsius))


def convertir(c):
    print((c * 1.8) + 32)


convertir(celsius)


def convertir(c):
    respuesta = 0
    respuesta = (c * 1.8) + 32
    return respuesta


print(convertir(celsius))
