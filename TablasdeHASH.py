# Las tablas hash (también conocidas como diccionarios en Python) son estructuras de datos que utilizan una función hash para asociar una clave a un valor. En Python, las tablas hash son implementadas mediante el uso de diccionarios, que son objetos mutables y pueden ser accedidos mediante llaves (clave) y devuelve un valor asociado.

# Un ejemplo de cómo se utiliza un diccionario en Python es:


telefonos = {"Juan": "555-555-5555", "Maria": "555-555-5556", "Pedro": "555-555-5557"}
telefonos["Juan"] # devuelve "555-555-5555"
telefonos["Maria"] = "555-555-5558" # actualiza el número de teléfono de Maria
telefonos["Ana"] = "555-555-5559" # agrega un nuevo nombre y número de teléfono
del telefonos["Pedro"] # elimina el nombre y número de teléfono de Pedro
# En esta ejemplo se crea un diccionario llamado "telefonos" con tres entradas, cada una con un nombre y un número de teléfono. Entonces se accede a los valores mediante las llaves correspondientes, se actualizan los valores y se eliminan entradas.

# Los diccionarios en Python son muy útiles para almacenar datos que deben ser accedidos rápidamente mediante una clave. En términos de rendimiento, las operaciones de búsqueda, inserción y eliminación tienen un tiempo de complejidad promedio O(1). Sin embargo, debes tener en cuenta que en algunos casos el rendimiento puede ser peor, ya que en caso de colisiones en la función hash el tiempo de complejidad puede ser O(n)

# Es importante también mencionar que python tiene algunas implementaciones de tablas hash con mayor rendimiento, como por ejemplo defaultdict y ordereddict.



