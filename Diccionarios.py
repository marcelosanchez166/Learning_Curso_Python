"""Ejercicio 1"""
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
#pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

# print("Ingrese el tipo de moneda que desea ver: ")
# print('Euro;', 'Dolar;', 'Yen')
# print('\n')
# moneda={'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
# valor=input("Ingrese el tipo de moneda: ")
# if valor=="Euro":
#           print("La divisa para la moneda ingresada es : ",moneda['Euro'])
# elif valor=="Dolar":
#           print("La divisa para la moneda ingresada es : ",moneda['Dolar'])
# elif valor=="Yen":
#           print("La divisa para la moneda ingresada es : ",moneda['Yen'])
# else:
#           print("La moneda no esta en la lista ")

"""#############################################################################################################"""

"""Ejercicio 2"""
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

# nombre=input("Ingrese su nombre: ")
# edad=int(input("Ingrese su edad: "))
# direccion=input("Ingrese su direccion de residencia: ")
# telefono=int(input("Escriba su numero de telefono: "))
# valores={"nombre":nombre, "edad":edad, "direccion":direccion, "telefono":telefono}

# print(valores["nombre"], ", ", "tiene ",valores["edad"],"años, ", "Vive en ",valores["direccion"],
# "Su numero de telefono es ",valores["telefono"])

"""Otra forma de hacerlo"""
# monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
# moneda = input("Introduce una divisa: ")
# if moneda.title() in monedas:
#           print(monedas[moneda.title()])
# else:
#           print("La divisa no está.")
"""#########################################################################################################"""

"""Ejercicio 3"""
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
#un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
#debe mostrar un mensaje informando de ello.
# print("\n")

# print("Fruta,   Precio")
# print("Plátano:  1.35")
# print("Manzana:  0.80")
# print("Naranja:  0.70")
# print("Pera   :  0.85")

# print("\n")

# frutas={'Platano':1.35, 'Manzana':0.80, 'Naranja':0.70, "Pera":0.85}
# fruta=input("Introduce una Fruta que desea comprar : ").title()
# kilos=float(input("Cuantos Kilogramos desea comprar: "))
# if fruta in frutas:
#           print("Costo por unidad ",frutas[fruta])
#           print(kilos, 'kilos de', fruta, 'valen: ', "$",frutas[fruta]*kilos, "dolares")
# else:
#           print("La fruta que ingreso no esta en el inventario ")
"""######################################################################################################################"""

"""Ejercicio 4"""
#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha 
#en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

# fecha=input("Ingrese una fecha con formato dd/mm/aaaa: ")
# fecha=fecha.split("/")#Lo que hace es como meterlo en una lista y por eso se puede acceder a ellos por el indice
# print(type(fecha))
# mes={1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo",6:"Junio", 7:"Julio",8:"Agosto",9:"Septiembre",10:"Octubre",11:"Noviembre",
# 12:"Diciembre"}
# print(fecha[0],mes[int(fecha[1])],fecha[2])
#En el pedazo mes[int(fecha[1])] lo que hace es que llama el diccionario y como el valor de entrada del mes se ingreso como float eje: 02
#lo comvierte a entero a 2 y luego llama la posicion de la lista fecha, e inmersamente el valor de la posicion 1 de la lista tendra
#el valor del item del diccionario ej: Febrero
"""######################################################################################################################"""

"""Ejercicio 5"""
#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
#{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato 
#<asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
#Al final debe mostrar también el número total de créditos del curso.

# notas=[]
# materias=['Matemáticas ', 'Física ', 'Quimica']
# for i in range(len(materias)):
#           print("Asignaturas: ",'Matemáticas ', 'Física ', 'Quimica')
#           nota=float(input("Ingrese para las notas de las materias: "+ materias[i]))
#           while nota<0 or nota>10:
                    
#                     nota=float(input("Ingrese para las notas de las materias: "))
                    
#           notas.append(nota)
# Asignaturas={'Matematicas': notas[0], 'Fisica': notas[1], 'Quimica': notas[2]}
# print("Para Matematicas su nota es: ",Asignaturas["Matematicas"],", " 
# "Nota para Física: ", Asignaturas["Fisica"],", ", "Calificacion para Quimica:", Asignaturas["Quimica"])


"""###############################################################################################################################"""


"""Ejercicio 6"""
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
#(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
#Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.


# info={}
# continuar= True
# while continuar==True:
#           print("Datos solicitados:  Nombre, edad, Sexo, Telefono, Correo electronico. ")
#           key=input("Que dato quiere introducir : ")
#           valor=input(key+ ": ")
#           info[key]=valor
#           print(info)
#           continuar= input('¿Quieres añadir más información (Si/No)? ').title()== "Si"

"""##########################################################################################################"""

"""Ejercicio 7"""
#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 
#el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar 
#por pantalla la lista de la compra y el coste total, con el siguiente formato
# total=0
# productos={}
# continuar= True
# while continuar==True:
#           print(" Ingrese el nombre del producto. ")
#           key=input("Nombre del producto : ")
#           valor=float(input("Precio para el producto "+key+ ": "))
#           productos[key]=valor
#           #total=valor+total
#           continuar= input('¿Quieres añadir otro producto (Si/No)? ').title()== "Si"
# for key, valor in productos.items():
#           print(key, ' \t ', "$", valor)#EL \t significa una tabulacion 
#           total += valor
# #print(productos)
# print("El costo total por los productos es ",total)

"""###########################################################################################################################"""

"""Ejercicio 8"""
#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en 
#español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear 
#un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para 
#traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

# Diccionario={}
# palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")

# for i in palabras.split(","):#El .split(",")Separa las palabras con comas o puntos segun le pongamos
#           english,spanish=i.split(":")
#           Diccionario[spanish]=english
# frase=input("Ingrese una frase: ")
# for i in frase.split():
#           if i in Diccionario:
#                     print(Diccionario[i], end=' ')
#           else:
#                     print(i, end=' ')

"""########################################################################################################################"""


"""Ejercicio 9"""
#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en 
#un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. 
#El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
#Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
#Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación 
#el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

# print("Sistema de almacenamiento de facturas y pago de facturas \n... ")
# Diccionario={}
# #continuar=True
# seguir=""
# pendiente = 0
# while seguir!="salir":
#           """#Factura = input("Ingrese el numero correlativo de la factura: ")
#           #claveN=input("Ingrese el numero correlativo de la factura:   ")
#           #valorC=float(input("Monto total de la factura : "+claveN + ": "))
#           #Diccionario[claveN]=valorC
#           #seguir= input('¿Quieres añadir otra factura o pagar una factura existente (Agregar/Pagar/salir)? ').lower()
#           #print(continuar)"""
#           if seguir=="agregar":
#                     claveN=input("Ingrese el numero correlativo de la factura:   ")
#                     valorC=float(input("Monto total de la factura : "+claveN + ": "))
#                     Diccionario[claveN]=valorC
#                     #continuar= input('¿Desea continuar agregando facturas (Si/No)? ').title()== "Si"
#                     pendiente +=valorC
#           elif seguir=="pagar":
#                               claveN=input("Ingrese la clave de la factura a pagar: ")
#                               del Diccionario[claveN]
#                               pendiente -= valorC
#                               #continuar= input('¿Desea pagar otra factura (Si/No)? ').title()== "Si"
#                               print("Cantidad cobrada de la factura "," $",valorC)
#                               print ("Facturas pendiente de Cobro: ",Diccionario)
#                               print('Pendiente de cobro: ', pendiente)
#           seguir= input('¿Quieres añadir otra factura o pagar una factura existente (Agregar/Pagar/salir)? ').lower()
#           print(" Adios... ")


"""##########################################################################################################################"""

#Ejercicio 10
#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en 
#un diccionario en el que la clave de cada cliente será su DUI, y el valor será otro diccionario con los datos del cliente 
#(nombre, dirección, teléfono, correo, preferente), donde el valor preferente tendrá el valor True si se trata de un cliente preferente. 
#El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
#(4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá 
#que hacer lo siguiente:

# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el DUI del cliente y eliminar sus datos de la base de datos.
# Preguntar por el DUI del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su DUI y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su DUI y nombre.
# Terminar el programa.

# print("Gestion de clientes para la empresa de Weones \n... ")
# base_datos={}
# cliente={}
# seguir=""
# while seguir!="salir":
#           if seguir=="agregar" or seguir=="1" :
#                     dui=input("Ingrese su DUI: ")
#                     name=input("Nombre del cliente: ")
#                     address=input("Ingrese su Direccion: ")
#                     phone=input("Numero de telefono: ")
#                     mail=input("Ingrese su correo electronico: ")
#                     tipo_cliente=input('¿Es un cliente preferente (Si/No) ? ').lower()
#                     base_datos["Nombre"]=name
#                     base_datos["direccion"]=address
#                     base_datos["telefono"]=phone
#                     base_datos["correo"]=mail
#                     base_datos["preferente"]=tipo_cliente
#                     base_datos={"Nombre":name,"dirección":address,"teléfono":phone,"correo":mail,"preferente":tipo_cliente=="si"}
#                     cliente[dui] = base_datos
#                     print("Cliente agregado exitosamente")

#           if seguir=="eliminar" or seguir=="2":
#                     dui=input("introduce del cliente a eliminar ")
#                     if dui in cliente:
#                               del cliente[dui]
#                               print("Cliente con Dui "+ cliente[dui]+ "eliminado")
#                     else:
#                               print("El numero de Dui del Cliente no existe ")

#           if seguir=="mostrar" or seguir=="3":
#                     dui = input('Introduce el numero de dui del cliente: ')
#                     if dui in cliente:
#                               print('Dui:', dui)
#                               for clave, valor in cliente[dui].items():
#                                         print(clave.title() + ':', valor, "\n")
#                     else:
#                               print('No existe el cliente con el nif', dui)

#           if seguir=="listar clientes" or seguir=="4":
#                     for clave, valor in cliente.items():
#                               print(clave, valor['Nombre'])

#           if seguir=="5" or seguir=="clientes preferentes":
#                     print('Lista de clientes preferentes')
#                     for clave, valor in cliente.items():
#                               if valor['preferente']:
#                                         print(clave, valor['Nombre'])
#                               else:
#                                         print("No hay clientes preferentes")

#           if seguir=="terminar" or seguir=="6":
#                               break

#           seguir= input(" (1) Agregar \n (2) Eliminar \n (3) Mostrar cliente \n (4) Listar todos los clientes \n" 
#           " (5) Listar clientes preferentes \n (6) Terminar \n Elige una opción: ").lower()


# print(base_datos)
# #Datos_unificados={Dui:base_datos}


"""#################################################################################################################"""

"""Ejercicio 11"""
#El directorio de los clientes de una empresa está organizado en una cadena de texto como la de más abajo, 
#donde cada línea contiene la información del nombre, email, teléfono, nif, y el descuento que se le aplica. 
#Las líneas se separan con el carácter de cambio de línea \n y la primera línea contiene los nombres de los campos 
#con la información contenida en el directorio.
"""nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

#Escribir un programa que genere un diccionario con la información del directorio, donde cada elemento corresponda 
#a un cliente y tenga por clave su nif y por valor otro diccionario con el resto de la información del cliente. 
#Los diccionarios con la información de cada cliente tendrán como claves los nombres de los campos y como valores 
#la información de cada cliente correspondientes a los campos. Es decir, un diccionario como el siguiente
"""{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}"""



# Cadena con los datos de los clientes de la empresa
datos_clientes = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
# Dividimos la cadena por el caracter de cambio de línea \n y creamos una lista con las subcadenas
lista_clientes = datos_clientes.split('\n')
# Inicializamos el diccionario que va a contener el directorio de clientes a vacío.
directorio = {}
# Dividimos la cadena del primer elemento de la lista de clientes (que contienen los 
# nombres de los campos) por el caracter ; y creamos una lista con los campos.
lista_campos = lista_clientes[0].split(';') 
# Bucle iterativo para recorrer los elementos de la lista lista_clientes.
# la variable cliente recorre desde el segundo elemento hasta el último elemento de la lista 
# (el primer elemento contiene los nombres de campo así que no corresponde a un cliente)
for i in lista_clientes[1:]:
          # Inicializamos el diccionario que va a contener los datos del cliente actual a vacío.
          cliente = {}
          # Dividimos la cadena i por el caracter ; y creamos una lista con las subcadenas con la
          # # información del cliente
          lista_info = i.split(';') 
          # Bucle iterativo para recorrer los campos y añadir los pares al diccionario del cliente.
          # # j toma valores de 1 al número de campos menos 1. El primer elemento (posición 0) corresponde 
          # # al nif y no se añade al diccionario porque se utilizará después como clave en el diccionario
          # # principal
          for j in range(1,len(lista_campos)):
                    # Condicional. Si el campo actual es descuento convertimos su valor en real
                    if lista_campos[j] == 'descuento':
                              lista_info[j] = float(lista_info[j])
                              cliente[lista_campos[j]] = lista_info[j]
                              # Añadirmos un par al diccionario del directorio con la clave el nif del cliente y valor
                              # # el diccionario que acabamos de crear con el resto de sus datos.
                              directorio[lista_info[0]] = cliente
# Mostramos el diccionario por pantalla
print(directorio)