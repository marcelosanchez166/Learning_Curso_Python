# Fibonacci: Escribe un programa que calcule y muestre los primeros n números de la secuencia de Fibonacci.
def fibonacci(Nnumbers, first=0, second=1):
    result = [first, second]
    for i in range(2, Nnumbers):
        next_number = result[-1] + result[-2]
        result.append(next_number)
    return "Listado de numeros de la secuencia fibonacci del numero que ingreso {}".format(result)

Nnumbers=int(input("Ingrese un numero para calcular la serie fibonacci de ese numero: "))
print(fibonacci(Nnumbers,1,1))


# Suma de los n primeros números: Escribe un programa que calcule la suma de los primeros n números enteros.
def sumaNnumbers(numeros):
    suma=0
    for i in range(1,numeros+1):
        suma+=i
    return "La suma de los numeros anteriores al numero que ingreso es  {}".format(suma)

numeros=int(input("Ingrese un numero para calcular la suma de los primeros numeros: "))
print(sumaNnumbers(numeros))


# Números primos: Escribe un programa que determine si un número es primo o no.
def Primo_NoPrimo(number):
    if number%2 != 0:#Para saber si un numero es primo la division debe ser diferente de cero, si la division es exacta(cero) el numero no es primo
        return "El numero ingresado es primo {}".format(number)
    else:
        return "El numero ingresado NO es primo {}".format(number)

number=int(input("Ingrese un numero para saber si es primo o no: "))
print(Primo_NoPrimo(number))


# Ordenamiento de números: Escribe un programa que ordene un arreglo de números en orden ascendente o descendente.
def ordenamiento_numeros(ordenarlista):
    for i in range(len(ordenarlista)):
        for j in range(len(ordenarlista)):
            if ordenarlista[i] < ordenarlista[j]:
                temp=ordenarlista[i]
                ordenarlista[i]=ordenarlista[j]
                ordenarlista[j]=temp
    return "La lista queda ordenada de forma ascendente: {}".format(ordenarlista)

ordenarlista=[5,3,1,8,9,0]
print(ordenamiento_numeros(ordenarlista))


# Palíndromos: Escribe un programa que determine si una palabra es un palíndromo o no.
def palindromo(palabra):
    longitud=len(palabra)-1#Se le resta uno al string palabra para que cuando entre la condicion del ciclo comience desde el ultimo indice 
    #print(longitud)
    newword=""
    for i in range(longitud+1):#Le incremento mas 1 porque si no tomaria en cuenta el ultimo valor del string
        newword+=palabra[longitud]#Agrega cada valor de palabra[longitud] a newword por cada pasada que hace el ciclo mientras la condicion se cumpla
        #print(newword)
        longitud-=1#Decrementa en -1 el valor que tiene logitud Ej: al entrar al ciclo logitud tiene 3 indices cuando llega a esta linea hace 3-1=2 y vuelve a entrar al ciclo hasta llegar a 0
    if newword==palabra:
        return "La palabra {} ".format(newword) +"Si es palindromo."
    else:
        return "No es palindromo"

palabra="hola"
print(palindromo(palabra))


# Cifrado César: Escribe un programa que cifre y descifre mensajes utilizando el cifrado César.




# Cálculo de pi: Escribe un programa que calcule el valor de pi utilizando la fórmula de Leibniz.
def calcularPI(terms):
    pi=0
    for n in range(terms):
        pi += (-1.0)**n/(2.0*n+1.0)#Formula Leibniz para calcular PI con un rango de diezmil
    return 4*pi

print(calcularPI(10000))


# Juego de adivinanza: Escribe un programa que genere un número aleatorio y permita al usuario adivinarlo.




# Conversión de bases numéricas: Escribe un programa que convierta un número en un sistema numérico a otro sistema numérico.




# Cálculo de la mediana: Escribe un programa que calcule la mediana de un conjunto de números.