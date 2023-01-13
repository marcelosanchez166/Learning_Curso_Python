# Realice un programa que enumere los paises de la siguiente lista
# # paises = ['Canada', 'USA', 'Mexico', 'Australia']

# paises = ['Canada', 'USA', 'Mexico', 'Australia']
# for i in range(len(paises)):
#     print("Pais",i+1,paises[i])

# Crear un ciclo for que cuente de 0 a 100
# for num in range(0,101):
#     print(num)

# Haz una tabla de multiplicar utilizando el ciclo for
# numero=int(input("Ingrese un numero "))
# for tabla in range(11):
#     print(numero,"*",tabla,"=",numero*tabla)

#Imprima los números del 1 a 10 al revés utilizando el ciclo for
# for n in range(10,0,-1):
#     print(n)

# Crear un bucle que cuente todos los números pares hasta el 100
# for i in range(2,101,2):
#     if i%2==0:
#         print(i)

# Cree un bucle que sume los números del 100 al 200
# for i in range(100,200,1):
#     i=i+1
#     print(i)

# Dado un número, cuente el número total de dígitos de un número,
# Por ejemplo, el número es 75869, por lo que la salida debería ser 5.
# numero=str(75869)
# for i in range(1,len(numero)+1):
#     i=i+0
# print("el numero ingresado tiene ",i, "digitos", "los cuales son ", numero)


# Mostrar series de Fibonacci hasta 10 términos - Fibonacci con Python
# n=int(input("Enter the value of 'n': "))
#Programa para generar la secuencia fibonacci hasta  10
# n=10
# #Los primeros dos terminos son primero y segundo
# first=0
# second=1
# sum=0
# count=1
# print("Fibonacci Sequence: ")
# # Count deberia de ser mas que 10(n)
# while(count<=n):    
#     print(sum)
#     count+=1
#     first=second
#     second=sum
#     sum=first+second	

# Use un bucle para mostrar elementos de una lista dada que estén presentes en posiciones pares
# lista=[1,2,3,4,5,6,7,8]
# for i in range(1,len(lista)+1):
#     if i%2==0:
#         print(i)

# Escriba un programa en Python para imprimir todos los números primos entre 0 y 100 e imprima cuántos números primos hay.
for i in range(100):
    if i %i ==0:
        
        print(i)