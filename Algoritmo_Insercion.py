lista = [9, 81, 2, 3, 4, 1, 7, 6]
longitud = len(lista)

for i in range(1, len(lista)):
    print(lista)
    # En la primera iteracion del for el valor de actual es 81
    actual = lista[i]
    indice = i  # se guarda la posicion de i que seria la posicion 1 en la primera iterasion
    print("El indice actual para comparar es ", actual)
    # Entrará en el ciclo while si cumple las dos condiciones, si el indice es
    while indice > 0 and lista[indice-1] > actual:
        # mayor a la posicion cero y el valor de la lista indice menos 1 es mayor que el valor que contiene la variable actual
        # En la lista indice se guarda la posicion de la lista indice menos 1
        lista[indice] = lista[indice-1]
        indice = indice-1  # remplazo el valor de indice por el valor de indice menos 1
    lista[indice] = actual
print(lista)

