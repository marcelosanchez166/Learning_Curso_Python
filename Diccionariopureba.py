# Crea un diccionario vacío llamado person y agrega las claves "nombre", "apellido" y "edad" con valores para ti mismo.
person={}

person["nombre"]="Marcelo"
person["apellido"]="Sanchez"
person["edad"]=27
print(person)


# Crea una función que tome un diccionario como argumento e imprima cada clave y su valor en una línea separada. Llama a la función con el diccionario person que creaste en el ejercicio 1.
def imprimirclave(person):
    for key,value in person.items():
        print(key,value)

imprimirclave(person)


# Crea un diccionario que contenga los nombres de tus amigos como claves y sus números de teléfono como valores.
amigos={"josue":78221222,"Pablo":76332233,"lucas":72903322}


# Escribe una función que tome dos diccionarios como argumentos y devuelva un nuevo diccionario que combine los dos diccionarios. Si una clave aparece en ambos diccionarios, 
#el valor en el segundo diccionario debe usarse. Prueba la función con los diccionarios creados en los ejercicios 1 y 3.
"""Esta función toma dos diccionarios como argumentos, crea una copia del primer diccionario y luego actualiza esta copia con las claves y valores del segundo diccionario. 
De esta manera, si una clave aparece en ambos diccionarios, el valor del segundo diccionario sobrescribe al del primer diccionario."""
def CombinarDiccionarios(person,amigos):
  combined_dict = person.copy()
  combined_dict.update(amigos)
  return combined_dict

print(CombinarDiccionarios(person,amigos))

# Crea una función que tome un diccionario como argumento y devuelva el valor más grande en el diccionario. Si el diccionario está vacío, la función debe devolver None.
def returnmaxvalue(amigo):
    for  value in amigo.values():
        for values in amigo.values():
            if value<values:
                temp=values
                value=values
                values=temp
                return values
            else:
                None

amigo={"number1":78221222,"number2":76332233,"number3":999903322}
print(returnmaxvalue(amigo))

# Crea un diccionario que represente los precios de varios productos en una tienda. Los nombres de los productos deben ser las claves y los precios deben ser los valores.
diccproductos={"Tomates":0.10,"Cebollas":0.2,"platanos":0.50,"Limones":0.25,"Papas":0.15}


# Escribe una función que tome el diccionario de precios creado en el ejercicio 6 y un presupuesto como argumentos, y devuelva una lista de los nombres de los productos que se pueden comprar dentro del presupuesto.
def comprarproductos(diccproductos, presupuesto):
    productoscomprados={}
    for producto,precio in diccproductos.items():
        if precio<=presupuesto:
            presupuesto-=precio
            if producto in productoscomprados:
                productoscomprados[producto]+=1
            else:
                productoscomprados[producto]=1
    return productoscomprados
          


presupuesto=float(input("Cual es su presupesto para comprar: "))

print("Lista de productos que puede comprar con su presupuesto",comprarproductos(diccproductos,presupuesto))