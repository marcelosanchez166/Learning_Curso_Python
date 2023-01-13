"""Crear paquetes destribuibles"""

from setuptools import setup

setup(
name="Paquetesdistibuible",
version="1.0",
description="paquete distribuible de prueba",
author="Marcelo",
author_email="marcelosanchez166@gmail.com",
url="",
packages=["paquetes", "paquetes.PotenciaYRedondea"]

)
#hay que ejecutar desde el cmd o desde shell y ejecutar 
"""python setup.py sdist"""#para crear un paquete distribuible

#Despues hay que instalar el paquete en windows con el siguiente comando desde cmd o shell estando en la carpeta dist que se crea
"""pip3 install Paquetesdistibuible-1.0.tar.gz"""

#para desisntalar es lo mismo 
"""pip3 uninstall Paquetesdistibuible-1.0.tar.gz"""


"""CREANDO ESTE ARCHIVO SE PUEDE EJECUTAR EL ARCHIVO QUE SE COLOQUE EN LA OPCION PACKAGES DESDE CUALQUIER PARTE DE LA PC"""