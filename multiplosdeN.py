#Toma una entrada n y genera los números del 1 al n.
#Para cada múltiplo de 3, escriba 'Solo' en lugar del número.
#Para cada múltiplo de 5, imprime 'Aprender' en lugar del número.
#Para números que son múltiplos de 3 y 5, envíe 'SoloLearn'.

#Debe cambiar el código para omitir los números pares, 
#de modo que la lógica solo se aplique a los números impares en el rango.


n = int(input())
print("\n")

# en el for mete con paso dos para que le tome solo los numeros impares la primera vuelta x vale 1 en la segunda 3 tercera vuelta  y asi
for x in range(1, n,2):
          if x % 3 == 0 and x % 5 == 0: 
#este if nunca se va a cumplir porque el residuo de x % 3 y x % 5 NO va a ser cero al mismo tiempo y continua
                    print("SoloLearn")
                    continue
          elif x % 3 == 0:
                    print("Solo")
                    continue
          elif x % 5 == 0:
                    print("Learn")
                    continue
          else:
                    print(x)

"""for x in range(1, n, 2 ):
          if x % 3 == 0 and x % 5 == 0:
                    print("sololearn")
                    continue
          #elif x % 3 ==0 and x % 5==0 and x % 2 ==0:
          #         continue  
          elif x % 5 == 2 :
                    print("Solo")
          elif x % 5==0:
                    continue
          elif x % 3 ==1  and x % 5 ==2 :
                    continue
          elif x % 5 ==4:
                    print("learn")
                    continue
          #elif x % 3 ==5:
          #          continue
          elif x % 3 ==0:
                    continue
          else:
                    print(x)"""
"""1
Solo
Learn
7
Solo
11
13"""