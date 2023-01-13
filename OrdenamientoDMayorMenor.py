#Para este ejercicio será necesario crees un script el cual sea capaz de ordernar, de forma descendente,
#tres números positivos. El script debe cumplir las siguientes reglas.
#El usuarios debe ser capaz de introducir (vía teclado) tres números de su conveniencia.
#El Script debe pedir, uno a uno, los números del usuario.
#El Script debe mostrar en consola, mediante un mensaje, los tres números ordenados de forma descendente.
#El mensaje será: El orden es: n1 - n2 - n3

n1=int(input("Ingrese un numero entero : "))
n2=int(input("Ingrese un 2do numero entero : "))
n3=int(input("Ingrese un 3er numero entero : "))
mayor=0
medio=0
menor=0
if n1>n2 and n1>n3:
          mayor=n1
          if n2>n3:
                    medio=n2
                    menor=n3
          else:
                    medio=n3
                    menor=n2
elif n2>n1 and n2>n3:
          mayor=n2
          if n1>n3:
                    medio=n1
                    menor=n3
          else:
                    medio=n3
                    menor=n1
else:
          mayor=n3
          if n1>n2:
                    medio=n1
                    menor=n2
          else:
                    medio=n2
                    menor=n1
print("El orden es: ", mayor, "-", medio, "-", menor)


