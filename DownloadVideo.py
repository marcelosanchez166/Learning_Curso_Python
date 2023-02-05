#Hay que instalar primero el paquete 
#pip install pytube

import pytube

link=input("Ingrese la url del video ")
yt=pytube.YouTube(link)
yt.streams.first().download()
print("Dowloaded", link)
