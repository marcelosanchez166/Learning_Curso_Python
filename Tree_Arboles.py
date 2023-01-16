# Un árbol (Tree) es una estructura de datos que consiste en un conjunto de nodos conectados mediante enlaces. En Python, hay varias formas de implementar un árbol, pero aquí hay algunos ejemplos de cómo se puede hacerlo:

# Utilizando una clase Node:

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

root = Node(1)
child1 = Node(2)
child2 = Node(3)
root.children = [child1, child2]
# En este ejemplo, se crea una clase Node que tiene un atributo de datos y una lista de hijos. Luego se crean tres objetos Node, uno para la raíz y dos para los hijos, y se establece la relación padre-hijo entre ellos.

# Utilizando un diccionario:

tree = {1: [2,3], 2: [4,5], 3: [6,7]}
# En este ejemplo, se utiliza un diccionario para representar un árbol, donde la clave es el nodo padre y el valor es una lista de los hijos.

# Utilizando una librería de terceros como "anytree":

from anytree import Node, RenderTree
root = Node("root")
child1 = Node("child1", parent=root)
child2 = Node("child2", parent=root)
print(RenderTree(root))
# En este ejemplo se utiliza la librería anytree para crear un árbol y se usa el método RenderTree para imprimir la estructura del árbol.

# Hay muchas otras formas de implementar un árbol en Python, y la elección dependerá de las necesidades específicas de tu aplicación. Es importante que sepas que las operaciones comunes en árboles son: búsqueda, inserción, eliminación, recorridos (como in-order, pre-order, post-order) y su tiempo de complejidad depende de la implementación y la estructura del árbol.



