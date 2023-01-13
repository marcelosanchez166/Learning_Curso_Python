lista = [23, 333, 42, 25, 46, 47, 15, 34, 89, 42]

for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[j] > lista[i]:
            temporal = lista[j]
            lista[j] = lista[i]
            lista[i] = temporal
print(lista)


lista1 = [332, 44, 55, 664, 7, 88, 929, 100]
for i in range(len(lista1)):
    for j in range(len(lista1)):
        if lista1[i] < lista1[j]:
            temporal = lista1[j]
            lista1[j] = lista1[i]
            lista1[i] = temporal
print(lista1)


lista2 = [99, 44, 34, 222, 45, 90, 1000, 45]
for i in range(len(lista2)-1):
    for j in range(len(lista2)-1):
        if lista2[j] > lista2[j+1]:
            temporal = lista2[j]
            lista2[j] = lista2[j+1]
            lista2[j+1] = temporal
print(lista2)
