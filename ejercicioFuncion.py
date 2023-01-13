#El código dado toma un texto y una palabra como entrada y los pasa a una función llamada búsqueda ().
#La función de búsqueda () debe devolver 'Palabra encontrada' si la palabra está presente en el texto, o 'Palabra no encontrada'
#si no lo está.

#Se define una funcion y dentro de ella se pone el codigo de lo que hara
"""def seacrh(text,word) :
          if word in text : #en el if pregunta si la palabra que ingreso el user existe en el texto que imprima palabra encontrada
                    print ('Word found')
          else:
                    print('Word not found')#si no esta imprime palabra no encontrada
text = input()
word = input()
seacrh(text,word)"""


def seacrh(text,word) :
          if word in text :
                    print ('Word found')
          else:
                    print('Word not found')
text = input("Ingrese un texto: ")
word = input("ingrese una palabra: ")
seacrh(text,word)