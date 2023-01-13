##Juego del ahorcado
import random

print("Bienvenido al Juego de Ahorcado  \n ")
print("Tienes 15 Intentos  ")

word = ['pan' , 'sopa', 'murcielago', 'tomates', 'casa']
intentos=15
letra=[]
i=1
indice=0
def word2(word):
          indice=random.randint(0,len (word)-1)

pal=word[indice]
letramayus=pal.upper()
letrapri=letramayus[0]
letraultima=letramayus[-1]
n=len(letramayus)-2
subguion=n * " _ "
pista=letrapri + subguion + letraultima
print(pista)


while i<=intentos:
          letter=input("Ingrese una letra : ")
          if letter in pal:
                    print("la letra existe en la palabra ")
                    letra.append(letter)
                    print("Te quedan ",intentos-i, "oportunidades ")
                    print(letra)
                    break
else:
          print("la letra no existe en la palabra ")
          print("Te quedan ", intentos-i )
i+=1                 

#str_match = [s for s in my_list if letra in s]
#print(str_match)
#print(correo[:correo.find('@')] + '@ceu.es' )




"""def word2(word):
          random.choice(word)
          for i in range(intentos):
                    if letter in word:
                              print("la letra existe en la palabra ")
                              print("Te quedan ", intentos-1, "oportunidades ")
                    else:
                              print("la letra no existe en la palabra ")
                              print("Te quedan ", intentos-1, "Intentos ")
                              i=+1              """
#print(letter)
#print(word2(word))
#return random.choice(word)