Lista = [9, 21, 2, 34, 5, 66, 6,1]

for i in range(len(Lista)):
    for j in range(len(Lista)):
            if Lista[i]<Lista[j]:
                temp=Lista[i]
                Lista[i]=Lista[j]
                Lista[j]=temp
print(Lista)