#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza 
# aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu.
#Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le 
# muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y 
# el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los 
# ingredientes que lleva.

print("Binvenido a Pizzeria Bella Napoli \n")
print("=====================MENU=========================== \n")
print("Escriba 1, Para la Pizza Vengetariana    ")
print("Escriba 2, Para la Pizza no Vegentariana.  \n")
TipoPizza=int(input("Ingrese la opcion de la pizza que desea ordenar "))
print("\n")
if TipoPizza==1:
          print("Puede elegir Uno de los 2 ingredientes para su pizza vegetariana \n")
          print("Ingredientes Pimientos o Tofu \n")
          IngredienteV=input("Ingrese el ingrediente de su Pizza Vegentariana ")
          print("\n")
          print("Gracias por vistarnos su pizza Vegetariana incluye los ingredientes \n")
          print("Pizza vegetariana con mozzarella, salsa de tomate y ", IngredienteV, "Esta lista \n")
if TipoPizza==2:
          print("Elija uno de los 3 ingredientes para su pizza No Vegetariana \n")
          print("Ingredientes: Peperoni, Jamón y Salmón. \n")
          IngredienteV=input("Ingrese el ingrediente de su Pizza No vegentariana ")
          print("\n")
          print("Gracias por vistarnos su pizza No Vegetariana incluye los ingredientes \n")
          print("Pizza No vegetariana con mozzarella, salsa de tomate y ", IngredienteV, "Esta lista \n ")
print("Gracias por su compra, Vuelva pronto ")

