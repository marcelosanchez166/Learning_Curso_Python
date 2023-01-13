# Si se llama a range con un argumento, producirá un objeto con valores de 0 a ese argumento.
# Si se llama con dos argumentos, producirá valores del primero al segundo.

# También hay un tercer argumento que puede usar con range ()
# y es realmente útil. Se llama step y determina el intervalo de la secuencia producida. Echar un vistazo:
nums = list(range(3, 15, 3))  # imprime la posicion 2 del range que es 9
print(nums[2])

print("\n")

for i in range(5):  # imprime cinco veces hello
    print("hello")
print("\n")

for i in range(0, 20, 2):
    # este for imprime los numero pares entre cero a 20 el tercer numero en el range()
    print(i)
# indica si es de dos en dos o tres en tres

print("\n")

# imprime los numeros de la lista segun su posicion sin contar la ultima posicion
squares = [0, 11, 20, 51, 43, 56, 67, 79, 81, 91, 110]
print(squares[2:6])  # imprime el [20,51,43,56]
print(squares[3:8])  # imprime los valores[51,43,56,67,79]
print(squares[0:1])  # imprime los valores [0]
print("\n")

# Si se omite el primer número de un segmento, se considera que es el comienzo de la lista.
# Si se omite el segundo número, se considera que es el final.
squares = [0, 11, 20, 51, 43, 56, 67, 79, 81, 91, 110]
print(squares[:6])  # imprime las primera 6 posiciones de la lista
print(squares[7:])  # imprime los numeros desde la posicion 7 asta el ultimo

print("\n")
# Al igual que con los rangos, los sectores de la lista pueden incluir un tercer número,
# que representa el paso, para incluir solo valores alternativos en el sector.
squares = [0, 11, 20, 51, 43, 56, 67, 79, 81, 91, 110]
# imprime los valores de dos en dos ej:[0, 20, 43, 67, 81, 110]
print(squares[::2])
# imprime los valores de tres en tres asta la posicion 8 ej:[20, 56]
print(squares[2:8:3])


print("\n")
# Otro ejemplo de lista
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# La salida es desde la posicion 1 asta el ultimo con paso 4 osea de cuantro en cuatro
print(sqs[1::4])


print("\n")
# los valores negativos también se pueden usar en la división de listas (así como en la indexación de listas normal).
# Lo que significa que cuando se utilizan valores negativos para el primer y segundo valor en un segmento
# (o un índice normal), cuentan desde el final de la lista
squares = [0, 11, 20, 51, 43, 56, 67, 79, 81, 91, 110]
# Imprimer la posicion 1 asta la posicion -3 en este caso asta el 79 ej:[11, 20, 51, 43, 56, 67, 79]
print(squares[1:-3])

print("\n")

# Si se usa un valor negativo para el paso, el corte se hará al revés.
# Usar [:: - 1] como un segmento es una forma común e idiomática de invertir una lista.
squares = [0, 11, 20, 51, 43, 56, 67, 79, 81, 91, 110]
# Imprime todos los valores desde el ultimo numero de la lista asta el primero en orden invertido(el ultimo sera el primero)
print(squares[::-1])
#ej:[110, 91, 81, 79, 67, 56, 43, 51, 20, 11, 0]


print("\n")
# ejemplo
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# Imprime desde la posicion 7 asta la 5 sin incluirla contando desde el ultimo numero, los valores que se muestran son
print(sqs[7:5:-1])
#[36, 49]

print("\n")
# ejemplo2
list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
# imprime la 5 posicion


print("\n")
# Ejemplo con for y range
for i in range(10):
    if not i % 2 == 0:  # si el reciduo de i%2 no es igual a cero va imprimir i+1
        print(i+1)  # si el residuo es igual a cero no lo imprime pero si le suma uno


print("\n")
# ejemplo3
list = [1, 2, 3]
for var in list:
    print(var)  # si pongo la variable var me muestra los valores de la lista
# print(list) Si pongo la variable list imprimira 3 veces la lista asi #[1, 2, 3] #[1, 2, 3] #[1, 2, 3]

print("\n")
# Ejemplo 4
x = [6, 4, 2, 9]
x = x[::-1]  # aqui las desordena y quedan [9,2,4,6]
# imprime la suma de la posicion cero y la posicion2 que serian los valores de 9 y 4 que es = 13
print(x[0]+x[2])
