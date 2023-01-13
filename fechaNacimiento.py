#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, 
#el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un 
#solo carácter.

fecha=input("ingrese su fecha de nacimiento con el siguiete formato dd/mm/aaaa ")
print('Día ', fecha[:2] + ' Mes ', fecha[2:4] + ' Año ', fecha[4:10])
