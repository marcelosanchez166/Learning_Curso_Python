#A nadie le gusta la tarea, pero su profesor de matemáticas le ha asignado la tarea de encontrar 
#la suma de los primeros N números.
#¡Ahorremos algo de tiempo creando un programa que haga el cálculo por usted!
#Tome un número N como entrada y emita la suma de todos los números del 1 al N (incluido N).
N = int(input())
#your code goes here
suma=0
for i in range(1, N + 1):#suma desde 1 asta el numero que ingresa mas 1 para incluir el numero
          suma+=i#a la variable suma se le suma i y se guarda en ella misma luego se imprime
print(suma)