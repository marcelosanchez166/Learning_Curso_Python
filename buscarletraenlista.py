my_list = ['pan', 'tomates', 'jueves', 'titulo']
letra=input("ingrese una letra " )
str_match = [s for s in my_list if letra in s]
print(str_match)