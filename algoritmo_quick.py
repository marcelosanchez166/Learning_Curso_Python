def quick_sort(numbers):
    if len(numbers)<2:
        print(numbers)
        return numbers
    pivote=numbers[-1]
    menores, iguales, mayores=[],[],[]
    
    for i in numbers:
        if i<pivote:
            menores.append(i)
        if i == pivote:
            iguales.append(i)
        if i > pivote:
            mayores.append(i)
    return quick_sort(menores)+iguales+quick_sort(mayores)

numbers=quick_sort([5,1,5,2,8,3,9])
print(numbers)