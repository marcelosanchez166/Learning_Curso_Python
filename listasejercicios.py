#1- Crea un array con los numero 10, 20, 30, 40, 50 y luego muestra los que hay en las posiciones impares """
#2-Pide al usuario 10 numeros y luego mustra los que son impares con array
#3-Pide al usuario un numero entero del 1 al 12 y escribe el nombre del mes correspondiente usando un array 


#1- Crea un array con los numero 10, 20, 30, 40, 50 y luego muestra los que hay en las posiciones impares
num=[10,20,30,40,50]
n=0
for n in range(len(num)):
          if n % num[n]==1 or n%num[n]==3:
                    print(num[n])
                    #print(i,"="+str(num[3]))


#2-Pide al usuario 10 numeros y luego mustra los que son impares con array
array=[]
varn=10
for i in range(varn):
          numero=int(input("Ingrese un numero: "))
          array.append(numero)
          i+=i
print("Los numero que ingreso son: ", array)


#3-Pide al usuario un numero entero del 1 al 12 y escribe el nombre del mes correspondiente usando un array 

mesarray=["Ene", "febre", "marz", "abril", "mayo", "juni","julio", "agost","sep","octu","nov","Dici"]
numero=int(input("Ingrese un numero del 1 al 12 : "))
numero-=1
#i=1
for i in range(len(mesarray)):
          
          #if numero >13:
          #          print("Numero Fuera de rango: ")
          if mesarray == mesarray[numero]:
                    mesarray[numero]
print(mesarray[numero])