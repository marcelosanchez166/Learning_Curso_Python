# ¿Por qué se utiliza If __name__ == '__main__'?


# Si eres una persona nueva en el desarrollo en Python, sin duda alguna, en algún momento de tu carrera, te habrás topado con la siguiente condición. 🐍

# if __name__ == '__main__':
#     pass
# Condición que, regularmente se utiliza como puerta de entrada para poder ejecutar nuestro programa en Python. Algo muy similar a lo que podemos encontrar con otros lenguajes de programación con las funciones o métodos principales main.

# C.

# int main() {
#    // C Code.
# }
# Rust.

# fn main() {
#     //  Rust Code
# }
# Java.

#  public static void main(String[] args) {
#     // Java Code.
# }
# Sin embargo, si bien la condición en Python sí permite ejecutar nuestro programa, también es importante mencionar que no es necesaria. 😵 Sí, así como lo lees, podemos, o no, utilizar.

# Entonces ¿Cómo funciona? 🙃

# Bueno, para poder comprender al 100% cuando utilizar, o no, dicha condición, primero debemos conocer cómo Python ejecuta nuestros proyectos. Es por ello que, para esta nueva entrega de PyWombat, me gustarías habláramos sobre módulos en Python.

# Un tema super importante si quieres dar el siguiente paso en el desarrollo con Python.

# Será un post sumamente interesante, así que te invito a que te quedes.

# Bien, si más introducción, pongamos manos a la obra.

# Módulos en Python 🐛
# Comencemos con lo principal y respondamos a la pregunta ¿Qué es un módulo? 😋

# Bueno, como sabemos, para pode ejecutar nuestro código Python, lo habitual es guardar dicho código en archivos con extensión .py. Pues bien, ha estos archivos los conoceremos como módulos.

# Los módulos pueden tener todo el código Python que deseemos. Desde una sola línea de código, pasando cien, mil o inclusive más.

# Aquí un pequeño ejemplo.

# main.py

# print('Hola, nos encontramos en un nuevo post de PyWombat')
# Si ejecutamos el script en terminal deberíamos poder visualizar nuestro mensaje en consola.

# python main.py
# Hola, nos encontramos en un nuevo post de PyWombat
# El ejecutar el módulo todo, el código que se encuentre en él será ejecutado.

# Hasta aquí, probablemente, nada nuevo. 🧐

# Sin embargo ¿Qué pasa si no ejecutamos el módulo directo en terminal, si no que, por el contrario, lo importamos? 😲

# Para ello vamos a ingresar al shell de Python.

# Nota: Del tema de imporst ya hemos hablado anteriormente. Te comparto el link del post para que le eches un vistazo.

# >>> import main
# Hola, nos encontramos en un nuevo post de PyWombat
# Para este segundo ejemplo ocurre algo muy particular. Inmediatamente después de importar el módulo visualizamos en consola el mensaje del script.

# Este comportamiento se debe a cómo el interprete de Python maneja los módulos.

# Verás, cuando ejecutamos directamente el módulo en terminal, o lo importamos, Python ejecutara todo el código que se encuentra en él. Creando variables, funciones, clases, método, condiciones, ciclos etc... Todo el código, reitero, será ejecutado.

# Es por ello que, obtenemos ese comportamiento. Una vez importado el modulo visualizamos en consola el mensaje.

# Si esto aun no te queda del todo claro, no te preocupes, compliquemos un poco más nuestro ejemplo.

# main.py

# print("Antes de crear la función Suma")

# def suma(a, b):
#     return a + b

# print("Antes de crear la función Resta")

# def resta(a, b):
#     return a - b

# print("Antes de crear la función Multiplicación")

# def multiplicacion(a, b):
#     return a * b

# print("Antes de crear la función División")

# def division(a, b):
#     return a / b

# resultado = suma(10, 20)
# print(resultado)
# Si importamos nuevamente veremos como el módulo se ejecuta en su totalidad.

# >>> import main
# Antes de crear la función Suma
# Antes de crear la función Resta
# Antes de crear la función Multiplicación
# Antes de crear la función División
# 30
# Lo interesante de todo esto es que, al ejecutar o importar un módulo, Python asigna un nuevo atributo a él, llamado __name__ (Recordemos que Python todo es un objeto, y los módulos también lo son). 😉

# Dependiendo del contexto donde se ejecute el módulo ,el valor de este atributo será diferente.

# Veamos.

# Si el módulo es importando, el valor de su atributo será el mismo que el nombre del script. 😛

# >>> main.__name__
# 'main'
# Sin embargo, si ejecutamos el módulo directo por el interprete, en terminal, el atributo almacenará __main__. Haciendo alusión que es el módulo principal, y no se esta siendo importando de otro.

# main.py

# print(__name__)
# $ python3 main.py
# __main__
# Con todo esto en mente podemos concluir que la condición if __name__ == '__main__': permite ejecutar el código, sí, y solo sí, el módulo es el principal, es decir, fue ejecutado directamente con el interprete y no fue importado. 🐍

# Con todo este conocimiento podemos hacer un pequeño refctor a nuestro módulo principal. Quedando de la siguiente manera.

# def suma(a, b):
#     return a + b


# def resta(a, b):
#     return a - b


# def multiplicacion(a, b):
#     return a * b


# def division(a, b):
#     return a / b

# if __name__ == '__main__':
#     resultado = suma(10, 20)
#     print(resultado)
# Ahora, si importamos nuevamente no visualizaremos ningún tipo de mensaje, y podremos utilizar las funciones previamente definidas, ya que estas se encuentran antes de la condición.

# >>> import main
# >>> main.suma(10, 20)
# 30
# Perfecto. 🤯

# ¿Cuándo condicionar?
# Ya para finalizar debemos responder a la pregunta ¿Cuándo utilizar esta condición? 🧐

# La respuesta es relativamente sencilla, siempre. Bueno, no tanto así. Siempre que podamos. 😅

# Si bien lo recomendable es hacer uso de la condición siempre que sepamos que el módulo puede ser tanto ejecutado como principal como puede ser importado, yo les recomiendo ampliamente usar la condición cuando el módulo comience a crecer, y comience a importar de otros módulos, ya que en un futuro, es probable, pase a ser parte de algo más grande (Quizás un paquete). 📦

# Aun que también debemos considera que un código con esta condición se ve mucho más elegante (Levanta el meñique). 🥂

# if __name__ == '__main__':
#     print('Hello World')
# Conclusión
# Ahora ya lo sabes, en Python los archivos con extensión .py los conoceremos como módulos. Y siempre que utilicemos un módulo, ya sea que lo ejecutamos o lo importemos, Python le asignará el atributo __name__, que podrá tomar diferente valor dependiendo de cómo el módulo se este llamando.

# Si el módulo es importado entonces el atributo tomará por valor el nombre del script, en caso contrario su valor será __main__. 🍻