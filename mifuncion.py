def my_func ():
          print ('spam')
          print ('spam')
          print ('spam')
my_func()

print("\n")

def print_with_exclamation (palabra):
          print (palabra + '!')
#Pasar los valores a la funcion cuando se manda a llamar
print_with_exclamation ('spam')
print_with_exclamation ('huevos')
print_with_exclamation ('python')

print("\n")

#le paso un valor y ese valor es asiganado a x y luego lo multiplica por 2
def print_double(x):
          print(2 * x)
print_double(4)

print("\n")

#Puede definir funciones con más de un argumento; Sepárelos con comas. 
def print_sum_twice (x, y):
          print(x + y)
          print(x + y)
print_sum_twice (5, 8)

print("\n")

#Ciertas funciones, como int o str, devuelven un valor en lugar de generarlo.
#El valor devuelto se puede utilizar más adelante en el código, por ejemplo, asignándolo a una variable.
#Para hacer esto para sus funciones definidas, puede usar la declaración de retorno
def max (x, y):
          if x >= y:
                    return x
          else:
                    return y
print (max (4, 7))
z = max (8, 5)
print(z)

print("\n")

def shortest_string(x, y): 
          if len(x) <= len(y):#hace la comparacion de la longitud de X y Y,
                    return x
          else:
                    return y
print(shortest_string("hola","mundo"))#le pasa los valores a la funcion y luego muestra el valor con menos longitud

print("\n")

#Define una función que tome dos números como argumentos y devuelve el más pequeño.
def min(x, y):
          if x<=y:
                    return x
          else:
                    return y
print(min(77,81))

print("\n")

def sum(x):
          res=0
          for i in range(x):
                    res +=i
          return res
print(sum(10))


print("\n")
def print_nums(x):
          for i in range(x):
                    print(i)
          return
print_nums(10)

print("\n")

def func(x):
          res = 0
          for i in range(x):
                    res += i
          return res
print(func(4))