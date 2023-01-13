from PIL import Image
import requests

#Para hacerlo mas intuitivo se podria pedir la url al usuario para que se descargue cualquier imagen deseada
url=input("Ingresa la url de la imagen a descargar: ")

#URL de la imagen a descargar
#url='https://sitio.com/photos/408701.jpeg'

#Nombre del archivo y su extension con la que se guardara la imagen
name='1139110.jpg'

#Tamaño de la imagen (ancho, alto)
size=(200, 200)

#Descargar la imagen y guardarla en la variable img
img=Image.open(requests.get(url, stream=True).raw)

#Cambiar el tamaño de la imagen al tamaño que se definio en la variable size
img=img.resize(size)

#Guardar la imagen en la carpeta deseada
img.save('imagenes/' + name)
