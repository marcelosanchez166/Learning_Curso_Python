#funcionamiento y sintaxis
"""Son funciones que a su vez añaden funcionalidades a otra funciones en el programa"""

#Estructura de los decoradores
"""La funcion decorador esta formada por tres funciones (A,B,C) Donde A es una funcion que recibe la otra funcion que en este ejemplo es B para poder devolver la Funcion C"""
#Un decorador devuelve una funcion y eso le da funcionalidad a la funcion con el decorador 

#Ejemplo de como funcionan los decoradores, La funcion A seria "Funcion_decorador" y la funcion B seria la "Funcion" que recibe la Funcion_decorador 
# y la funcion C seria "Funcion_interna()" Luego hay que retornar la Funcion C que seria return "Funcion_interna"
# def Funcion_decorador(Funcion):
#     def Funcion_interna():
#         pass
#         #Codigo de la funcion interna
#     return Funcion_interna


#Ejemplo1

#Funcion (A) Decorador
def Funcion_decorador(recibe_funcion):
    def Funcion_interior():#Funcion C
        #Funciones adicionales que decoran 
        print("Vamos a realizar un calculo: ")

        recibe_funcion()

        #Acciones adicionales que decoran 
        print("Hemos terminado el calculo")
    return Funcion_interior

@Funcion_decorador
def suma():
    print(15+20)


def resta():
    print(30-10)

suma()
resta()

#Decoradores 2 Con parametros 
