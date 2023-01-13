Crea tus propias excepciones en Python


En una entrega anterior, que te estaré dejando aquí, hablamos acerca de las excepciones en Python y sobre como manejarlas. Si recordamos utilizamos 4 nuevos bloques. 🐍

try
except
else
finally
Todo esto funciono bastante bien, y trabajamos con excepciones que el lenguaje ya posee. Así que, para esta segunda entrega, aprenderemos a crear nuestras propias excepciones. Excepciones custome que podremos definir para errores muy particulares.

Bien, sin más dilación comencemos con el post.

Excepciones propias. 🧐
Como mencionamos anteriormente todas las excepciones heredan de la clase padre Exception, por lo cual, para poder crear nuestra propia excepción debemos hacer exactamente los mismo. Crearemos una clase que herede de Exception.

class EmptyListError(Exception):
    pass
Para este ejemplo he creado el error EmptyList, un error que pretende lanzar siempre que nos encontremos con una listas vacía.

Pongamos a prueba nuestras excepción.

class EmptyListError(Exception):
    pass

def average(numbers):
    if not numbers:
        raise EmptyListError()

    return sum(numbers) / len(numbers) 
Para este nuevo ejemplo he defino la función average, que valida que el parámetro no sea una lista vacía. En caso lo fuera, entonces una excepción de tipo EmptyListError es lanzada. Para ello utilizamos la palabra reservada raise, simplemente lanza la excepción.

Si llamamos a la función con una lista vacía veremos nuestro error en consola.

>>> average([])

Traceback (most recent call last):
  File "main.py", line 11, in <module>
    average([])
  File "main.py", line 6, in average
    raise EmptyListError()
__main__.EmptyListError
Si bien el error es producido, no vemos mucha información acerca de él. Por lo tanto vamos hacer un refactor a nuestra clase error. 🐛

class EmptyListError(Exception):
    """Exception raised for empty lists

    Attributes:
        message
    """

    def __init__(self, message="Lo sentimos, la lista no puede estar vacía."):
        self.message = message

        super().__init__(self.message)
Ahora definimos el método init para poder establecer un mensaje de error. Si el mensaje no es dado al instanciar el de tipo EmptyListError, por default será: Lo sentimos, la lista no puede estar vacía.. Con esto le damos mucho más contexto al usuario de lo que esta pasando y el motivo del error.

Si ejecutamos nuevamente obtendremos el mensaje en consola.

Traceback (most recent call last):
  File "main.py", line 21, in <module>
    average([])
  File "main.py", line 16, in average
    raise EmptyListError()
__main__.EmptyListError: Lo sentimos, la lista no puede estar vacía.
Podemos cambiar el mensaje en la instancia del error. 😵

raise EmptyListError('La lista se encuentra vacía')
Perfecto.

Manejar errores propios 🦎
Al igual que con las excepciones que Python nos ofrece, las excepciones propias pueden ser manejadas con los bloques de try y except. Veamos un ejemplo.

try:
    promedio = average([])

except EmptyListError as err:
    print(err)

else:
    print('El promedio es:', promedio)
SI ejecutamos ahora visualizaremos en consola únicamente el mensaje de error.

Lo sentimos, la lista no puede estar vacía.
Más información en el error
Como hemos aprendido hasta ahora los errores podemos crearlos mediante clases, por lo tanto, al momento de instancias un nuevo error, es posible pasar la N cantidad de argumentos que deseemos, lo cual permite que nuestro error se construya con mucha más información.

Por ejemplo, creemos un error de Rango.

class RangoError(Exception):
    """Exception raised for rango number.

    Attributes:
        message
    """

    def __init__(self, number, message="Lo sentimos, el número se encuentra fuera de rango."):
        self.number = number
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return f'Number: {self.number} - {self.message}'
Para este nuevo error hemos definido el parámetro number, que permitirá conocer que número no se encuentra fuera del rango establecido. Así mismo hemos sobre escrito el método str para enriquecer aun más el mensaje de error.

En la instancia es posible pasar el número que no cumpla con el rango.

number = 10
if number > 0 and number < 215:
    raise RangoError(number)
Si ejecutamos encontraremos el mensaje mucho más personalizado.

Number: 10 - Lo sentimos, el número se encuentra fuera de rango.
Letras finales
Perfecto, ahora, con estos 2 post de Pywombat, tú ya puedes validar y crear tus propias excepciones en Python. Recuerda que las excepciones son necesarias para que un programa valide la mayor cantidad de casos de errores posibles.

No se trata de evitar los errores, si no aprender a lidiar con ellos. 🍻