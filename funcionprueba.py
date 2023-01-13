num=int(input("Ingrese un numero entero positivo "))
if num==1 or num==0:
          print ("1")
else:
          for i in range(1,num):
                    print(i)
                    factorial=i * num
          print(factorial)
print("Factorial of",num,"is", factorial)