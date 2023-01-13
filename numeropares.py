#pedir dos numeros por teclado y mostrar todos los numeros pares comprendidos entre ambos
numero1=int(input("Ingrese el primer numero "))
numero2=numero1
while numero2<=numero1:
          numero2=int(input("Ingrese un segundo numero "))
for i in range(numero1, numero2+1):
          if numero1 % 2 == 0:
                    print(i)