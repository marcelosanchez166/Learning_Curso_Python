# Escribe una función que reciba una lista de números y devuelva una lista que contenga solamente los números pares de la lista original.

def parsNumbers(lista):
    lista2=[]
    for i in lista:
        if i%2==0:
            lista2.append(i)
    return lista2

lista=[1,2,34,5,6,3,2,8,66]
print(parsNumbers(lista))


# Escribe una función que tome dos listas como argumentos y devuelva una lista que contenga los elementos comunes entre ambas listas.
def valorescomunes(lista1,lista2):
    lista=[]
    for i in lista1:
        for j in lista2:
            if i ==j:
                lista.append(i)
            continue
    return lista

lista1=[1,4,5,"Marcelo", "Juan"]
lista2=[1,2,3,"Juan","Luis","Marcelo"]
print(valorescomunes(lista1, lista2))


# Escribe una función que tome una cadena de texto como argumento y devuelva la longitud de la palabra más larga en la cadena.

def longitud(cadena):
    cade=cadena.split()
    count=""
    for i in cade:
        if i<count:
            count=i
        else:
            count=i
    return count

cadena="Hola como estas, espero que bien cuidate mucho bendiciones, ferrocarril"
print(longitud(cadena))


# Escribe una función que tome una lista de cadenas de texto y devuelva una lista con todas las palabras en la lista original ordenadas alfabéticamente.
def devolverlista(lista):
        lista.lower()
        lista.sort()
        return lista

lista=["Hola ","como", "estas","Espero" ,"que", "bien", "cuidate", "mucho","ella", "no", "te", "ama"]
print(devolverlista(lista))



# Escribe una función que tome una lista de números y devuelva el número más común en la lista.




# Escribe una función que tome un número entero como argumento y devuelva la suma de todos los dígitos del número.




# Escribe una función que tome una cadena de texto como argumento y devuelva la misma cadena con las letras en mayúscula y minúscula alternadas (por ejemplo, "Hola, mundo" -> "HoLa, MuNdO").




# Escribe una función que tome una lista de cadenas de texto y devuelva una lista con todas las palabras que empiezan con la letra "a".




# Escribe una función que tome una lista de números y devuelva una lista que contenga solamente los números impares de la lista original, ordenados de menor a mayor.




# Escribe una función que tome una cadena de texto como argumento y devuelva True si la cadena es un palíndromo (es decir, se lee igual de izquierda a derecha que de derecha a izquierda), o False en caso contrario.
