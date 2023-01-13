#Cuando sales a comer, siempre das una propina del 20% del importe de la factura. 
#Pero, ¿quién tiene tiempo para calcular la cantidad de propina correcta cada vez? ¡Tú no, eso es seguro! 
#Está creando un programa para calcular sugerencias y ahorrar algo de tiempo.
#Su programa necesita tomar el monto de la factura como entrada y sacar la propina como un flotador.
bill = int(input())
#your code goes here
bill=float(bill)
propina=(bill*20)/100
print(propina)