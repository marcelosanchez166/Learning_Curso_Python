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
        listanueva=[]
        for i in lista:
            list=i.lower()
            listanueva.append(list)
        listanueva.sort()
        return listanueva

lista=["Hola ","como", "estas","Espero" ,"que", "bien", "cuidate", "mucho","ella", "no", "te", "ama"]
print(devolverlista(lista))


# Escribe una función que tome una lista de números y devuelva el número más común en la lista.

def numeromascomun(numeros):
    max_count = 0
    comun = None
    counts = {}
    for num in numeros:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        if counts[num] > max_count:
            max_count = counts[num]
            comun = num
    print("El numero mas comun de la lista es ",comun)
    print(counts)


numeros=[2,2,4,5,6,7,8,9,9,7,7,66,42,22,2,3,3,3,3,3,44,5,5,6,]
numeromascomun(numeros)


# Escribe una función que tome un número entero como argumento y devuelva la suma de todos los dígitos del número.
def sumadigitos(number):
    suma=0
    for i in range(1,number+1):
        suma+=i
    return suma

number=5
print(sumadigitos(number))



# Escribe una función que tome una cadena de texto como argumento y devuelva la misma cadena con las letras en mayúscula y minúscula alternadas (por ejemplo, "Hola, mundo" -> "HoLa, MuNdO").
def convertircadena(cadena):
    cadena2=""
    debeser=True
    for i in range(len(cadena)):
        if cadena[i].isalpha():
            if debeser == True:
                cadena2 += cadena[i].upper()
            else:
                cadena2 += cadena[i].lower()
            debeser = not debeser #Por cada vez que sale del else la variable cambia su valor de false a true y viceversa
        else:
            cadena2 += cadena[i]
    return cadena2

cadena="Hola mundo, aprendiendo a, 23 programar, mejorando la logica"
print(convertircadena(cadena))


# Escribe una función que tome una lista de cadenas de texto y devuelva una lista con todas las palabras que empiezan con la letra "a".
def devolverlista(listacadena):
    palabrasconA=[]
    for i in listacadena:
        if "a" in i[0]:
            palabrasconA.append(i)
        else:
            continue
    return palabrasconA


listacadena=["Hola Genios","del mundo","del","mundo de ","la programacion","amamos","codear","tenemos","amor ","al codigo"]
print(devolverlista(listacadena))


# Escribe una función que tome una lista de números y devuelva una lista que contenga solamente los números impares de la lista original, ordenados de menor a mayor.

def devolvernumeroimpares(listanumeros):
    for i in listanumeros:
        if i%2!=0:
            listaordenada.append(i)
        else:
            continue
    for j in range(len(listaordenada)):
        for k in range(len(listaordenada)):
            if listaordenada[j]<listaordenada[k]:
                temp=listaordenada[j]
                listaordenada[j]=listaordenada[k]
                listaordenada[k]=temp
    return listaordenada

listaordenada=[]
listanumeros=[1,11,5,6,7,88,8,9]
print(devolvernumeroimpares(listanumeros))


# Escribe una función que tome una cadena de texto como argumento y devuelva True si la cadena es un palíndromo (es decir, se lee igual de izquierda a derecha que de derecha a izquierda), o False en caso contrario.
def palindromo(cadenapalindromo):
    inversa=cadenapalindromo[::-1]
    if inversa==cadenapalindromo:
        return "Es Palindromo"
    else:
        return "No es palindromo"

cadenapalindromo="radar"
print(palindromo(cadenapalindromo))