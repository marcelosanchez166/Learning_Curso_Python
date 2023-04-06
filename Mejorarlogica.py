# Escribir un algoritmo para encontrar el número más grande de una lista de números.
def numeromasgrande(listanumeros):
    number_max=0
    for i in range(len(listanumeros)):
        if listanumeros[i] > number_max:
            number_max=listanumeros[i]
        else:
            continue
    return number_max

listanumeros=[1,2,3,1000,4,99,5,6,7,8,9,100]
print(numeromasgrande(listanumeros))


# Escribir un algoritmo para encontrar el número más pequeño de una lista de números.
def numeromaspequeno(listanumeros):
    number_menor=0
    for i in range(len(listanumeros)):
        if listanumeros[i] < number_menor:
            number_menor=listanumeros[i]
        else:
            continue
    return number_menor

listanumeros=[1,2,3,1000,4,-3,99,5,6,7,8,9,100,0,-1]
print(numeromaspequeno(listanumeros))

# Escribir un algoritmo para calcular la suma de todos los números en una lista.
def sumadenumeros(numeroslista):
    suma=0
    for i in range(len(numeroslista)):
        suma+=numeroslista[i]
    return suma

numeroslista=[9,2,4,5,6]
print(sumadenumeros(numeroslista))

# Escribir un algoritmo para encontrar la media de una lista de números.
def calcularmedia(listamedia):
    suma=0
    for i in range(len(listamedia)):
        suma+=numeroslista[i]
    suma=suma/len(listamedia)
    return suma

listamedia=[6,7,4,3]
print(calcularmedia(listamedia))


# Escribir un algoritmo para encontrar la mediana de una lista de números.
def encontrarmediana(listamediana):
    count=0
    for i in range(len(listamediana)):
        for j in range(len(listamediana)):
            if listamediana[i]<listamediana[j]:
                temp=listamediana[i]
                listamediana[i]=listamediana[j]
                listamediana[j]=temp
    tamaño = len(listamediana)
    if tamaño % 2 == 1:
        indice_mediana = tamaño // 2
        return listamediana[indice_mediana]
    else:
        indice_mediana_1 = tamaño // 2 - 1
        indice_mediana_2 = tamaño // 2
        valor_1 = listamediana[indice_mediana_1]
        valor_2 = listamediana[indice_mediana_2]
        return (valor_1 + valor_2) / 2

listamediana=[2,3,4,5,6,5,6,4]
print(encontrarmediana(listamediana))

# Escribir un algoritmo para encontrar el modo de una lista de números.
def encontrarmoda(listamoda):
    moda={}
    moda_max=0
    for i in range(len(listamoda)):
        if listamoda[i] not in moda:
            moda[listamoda[i]]=1
        else:
            moda[listamoda[i]]+=1
        if moda[listamoda[i]]>moda_max:
            moda_max=moda[listamoda[i]]
    return "La moda es: {}, porque aparece {} veces en la lista.".format(moda_max, moda[moda_max])

listamoda=[12,3,4,6,77,5,4,3,3,12]
print(encontrarmoda(listamoda))


# Escribir un algoritmo para ordenar una lista de números en orden ascendente.
def ordenarlista(listaorden):
    for i in range(len(listaorden)):
        for j in range(len(listaorden)):
            if listaorden[i]<listaorden[j]:
                temp=listaorden[i]
                listaorden[i]=listaorden[j]
                listaorden[j]=temp
    print("La lista ordenada de forma ascendente es: ",listaorden)


listaorden=[3,2,5,6,1,7,9,8]
ordenarlista(listaorden)


# Escribir un algoritmo para ordenar una lista de números en orden descendente.
def ordenarlista(listadescendente):
    for i in range(len(listadescendente)):
        for j in range(len(listadescendente)):
            if listadescendente[i]>listadescendente[j]:
                temp=listadescendente[i]
                listadescendente[i]=listadescendente[j]
                listadescendente[j]=temp
    print("La lista ordenada de forma ascendente es: ",listadescendente)

listadescendente=[3,2,5,6,1,7,9,8]
ordenarlista(listadescendente)


# Escribir un algoritmo para encontrar el número de veces que un número aparece en una lista.
def Nveces(listanveces):
    maxnumber={}
    maxrepedito=0
    for i in range(len(listanveces)):
        if listanveces[i] not in maxnumber:
            maxnumber[listanveces[i]]=1
        else:
            maxnumber[listanveces[i]]+=1
    return "Numeros y cuantas veces aparecen en la lista. {} ".format(maxnumber)

listanveces=[4,6,7,98,0,9,8,8,8,4,3,3,2]
print(Nveces(listanveces))


# Escribir un algoritmo para invertir una lista de números.