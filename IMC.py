#El seguimiento de su IMC es una forma útil de comprobar si mantiene un peso saludable. 
#Se calcula utilizando el peso y la estatura de una persona, utilizando esta fórmula: peso / estatura²
#El número resultante indica una de las siguientes categorías:
#Peso insuficiente = menos de 18,5
#Normal = más o igual a 18,5 y menos de 25
#Sobrepeso = más o igual a 25 y menos de 30
#Obesidad = 30 o más
#Hagamos que averiguar su IMC sea más rápido y fácil, creando un programa que tome el peso y 
#la altura de una persona como entrada y genere la categoría de IMC correspondiente.

peso=int(input())
altura=float(input())
IMC=peso/float(altura)**2
if IMC < 18.5:
    print("Underweight " )
if IMC >=18.5 and IMC < 25:
    print("Normal  ")
if  IMC >=25 and IMC < 30:
    print("Overweight  ")
if IMC >= 30:
    print("Obesity  ")