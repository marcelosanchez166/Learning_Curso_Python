
def burbuja(lista1):
    for i in range(len(lista1)-1):
        #print(lista1[i])5,3,2,4,6
        #print[i]0,1,2,3,4
        #print[lista1][5, 3, 2, 4, 6],[5, 3, 2, 4, 6],[5, 3, 2, 4, 6],[5, 3, 2, 4, 6],[5, 3, 2, 4, 6]
        for k in range(len(lista1)-1):
            if lista1[k]>lista1[i]:
                temporal=lista1[k]
                lista1[k]=lista1[i]
                lista1[i]=lista1[k]

lista1=[5,3,2,4,6]
print(burbuja(lista1))


