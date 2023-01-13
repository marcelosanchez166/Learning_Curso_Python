lista = [9, 81, 2, 3, 4, 1, 7, 6]
longitud = len(lista)

for i in range(longitud-1):
    print(lista)
    menor = i
    print("El indice actual para comparar es ", menor)
    for j in range(i+1, longitud):
        if lista[j] < lista[menor]:  # compara si el indice que tiene j es menor que el que esta en i, la lista menor contiene el indice cero y su valor es 9
            menor = j  # Cambia el valor que tenia la variable menor en el primer ciclo con el indice j
            print("Recorriendo lista es menor el indice ", menor)
    # Aqui la variable temporal tiene guardado el valor menor que seria 1
    temporal = lista[menor]
    lista[menor] = lista[i]
    lista[i] = temporal
    print("Cambiamos el elemento ", lista[menor], "Por el elemento ", lista[i])
print(lista)
"""El ordenamiento por seleccion consiste en realizar la comparacion de la primera posicion contra la posicion cero, sabiendo esto el
siclo for comienza en la primera posicion de la lista"""
