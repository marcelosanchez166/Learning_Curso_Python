midiccionario3={23:"Jordan",
          "Nombre":"Michael", 
          "equipo":"Chicago", 
          "Anillos":[1991,1992,1993,1996,1997,1998]
}
print(midiccionario3)#Muestra todo el diccionario
print(midiccionario3[23])#Muestra solo el valor de la clave 23
print(midiccionario3["Anillos"])#Muestra los valores de la clave Anillos (osea todos los años)
print(midiccionario3["Anillos"][2])#Muestra el valor de la posicion 2 para la clave Anillos
print("\n")

print(midiccionario3.keys())
print("\n")
print(midiccionario3.values())
print("\n")
print(len(midiccionario3))