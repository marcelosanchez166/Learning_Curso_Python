bolsa=[]

Cprodu=int(input("Ingrese la cantidad de productos que desea comprar : "))

for i in range(Cprodu):
          producto=input("Ingrese el nombre del producto : ")
          bolsa.append(producto)
print("Los productos que compro son : ", bolsa)