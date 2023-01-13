#En este caso escribiria print("Divided by zero") pero si cambio por un valor divisible mostrara el resultado y print("the meaning of life")
#y si pongo un string mostrara print("ValueError or TypeError occurred")
try:
          meaning = 42
          print(meaning / 0)
          print("the meaning of life")
except (ValueError, TypeError):
          print("ValueError or TypeError occurred")
except ZeroDivisionError:
          print("Divided by zero") 

#####################################################################################################
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
          try :
                    return num1/num2
          except ZeroDivisionError:
                    print("No se puede dividir entre cero ")

while True:#Lo que hace este while es un bucle infinito asta que no se ingresen valores correctos osea numero enteros
          try:#intenta ejecutar las lineas de codigo si lo ingresado es correcto
                    op1=(int(input("Introduce el primer número: ")))
                    op2=(int(input("Introduce el segundo número: ")))
                    break #rompe el ciclo while cuando los valores son correctos
          except ValueError: #captura la excepcion y deja que el programa continue si hay algo mas despues
                    print("Los valores introducidos no son correctos. Intentalo de de nuevo")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print ("Operación no contemplada")
print("Operación ejecutada. Continuación de ejecúción del programa ")

#Tambien se puede poner un except globas sin pasarle ningun tipo de error y al momento de presentar error el programa 
#salta el print que se le alla puesto, Ej
# try:
#           op2=(int(input("Introduce el segundo número: ")))
# except:
#           print("Ha ocurrido un error")

#Tambien existe la instruccion finally que hace que lo que siga despues de cierta ejecucion de codigo y de error se ejecutara
#dicho codigo si esta despues del finally
#Ej: finally:


#Excepciones personalizadas con raise
#Para crear una excepcion personalizada se debe crear una clase con el error en concreto
#Para que se pueda dar la verdadera utilidad