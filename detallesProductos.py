#Escribir un programa que pregunte el nombre del producto, su precio y el número de unidades y muestre por pantalla 
#una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades 
#con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
canPrd=int(input("ingrese cuantos productos desea comprar "))
Acuprecio=0
NUnidad=0
for i in range (canPrd):
          producto=input("Esciba el nombre del producto ")
          precio=float(input("Ingrese el precio del producto "))
          unidades=int(input("cantidad de productos "))

          #acumuprod=str (acumuprod)+producto
          print("los productos que ingreso son ", producto, )
          #Acuprecio=float(Acuprecio)+precio
          print("el precio del producto es de  ", precio)
          #NUnidad=NUnidad+unidades
          print("la cantidad de productos es de ", unidades,("\n "))
          total1=precio*unidades
          Acuprecio=Acuprecio+total1
          i=i+1
total=Acuprecio
print("El total de su lista de productos es de ", total)
#print("los productos que ingreso son ", acumulador.replace(',', '\n'), "con valor de " "$",precio, "el numero de unidades es ", 
#unidades, "el total de su compra es de ", total)