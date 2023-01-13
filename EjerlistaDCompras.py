##Pedir al usuario que ingrese una lista de productos que quiere comprar
bolsa=[]
word=input("escriba Si para comprar, Escriba NO para salir : ")

while  word == "SI" or word =="si":
          producto=input("Ingrese el nombre del producto : ")
          
          if word=="si":
                    bolsa.append(producto)
                    word=input("Desea seguir comprando, SI, NO : ")
          else:
                    print("Adios Vuelva pronto: ")
print("Los productos que compro son : ", bolsa)