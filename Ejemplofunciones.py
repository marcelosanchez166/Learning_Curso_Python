#Crea una funcion que reciba 3 numeros y devuelva su suma
#Crea una funcion que reciba una cadena de texto y devuelva la cantidad de veces que la letra aparece dentro de la cadena
#Crea un procedimiento que escriba una linea formada por dos letras repetidas varias veces 
#


#1-) Crea una funcion que reciba 3 numeros y devuelva su suma
"""num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))

def suma(n1, n2, n3):
          return n1 + n2 + n3

print(suma(num1,num2,num3))"""

#2-) Crea una funcion que reciba una cadena de texto y devuelva la cantidad de veces que la letra aparece dentro de la cadena
"""string=input("Ingrese texto: ")
string=string.upper()
letra="T"
def texto(string1):
          print(string.count(letra))

texto(string)"""
##########################################################################################
#3-) Crea un procedimiento que escriba una linea formada por dos letras repetidas        #
#varias veces Ejem: para "-", "=" y 3 , escribiria "-=-=-="                              #
                                                                                          #
"""def linea(letra1, letra2, veces):                                                     #
          for i in range (veces):                                                        #
                    print(letra1,end="")                                                 #
                    print(letra2, end="")                                                #
                                                                                          #
linea("-", "=", 4)"""                                                                     #
                                                                                          #
                                                                                          #
word1=input("Ingrese una palabra: ")                                                      #
word1=word1.upper()                                                                       #
word2=input("Ingrese otra palabra: ")                                                     #
word2=word2.upper()                                                                       #
                                                                                          #
word3="A"                                                                                 #
word4="E"                                                                                 #
res=""                                                                                    #
res2=""                                                                                   #
def linea(letra1, letra2):                                                                #
          for i in range (len(word1)):                                                    #
                    res=word1.count(word3)                                                # 
                    resultado=(res * "-")  
                    print(resultado, end="")          
                                                                                          #
                    for n in range(len(word2)):                                           #
                              res2=word2.count(word4)
                              resultado2=(res2 * "=")
                    print(resultado2, end="")
                    break
                                                                                          #
                                                                                          #
linea(word1, word2)                                                                        #
##########################################################################################