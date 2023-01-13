# Archivos temporales
# Utilizando el módulo tempfile es posible crear archivos temporales, archivos en los cuales es posible escribir y leer información.

# Por default al instanciar TemporaryFile solo será posible escribir bytes, sin embargo si pasamos como argumento 'w+t' 
# podremos escribir strings.

import tempfile 

print("Nuevo archivo temporal")

temp = tempfile.TemporaryFile('w+t')
try:
    print("Nombre del archivo:", temp.name)

    temp.write('Hola mundo\n')
    temp.write('Nos encontramos en un archivo temporal')

    # Nos situamos al inicio del archivo
    temp.seek(0)

    content = temp.read()
    print(content)

finally:
    temp.close()