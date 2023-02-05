#Para poder crear archivos ejecutables de un programa python hay que instalar la herramienta ----pyinstaller----
#Se instala desde una consola cmd o desde visual studio con el comando 
#      pip install pyinstaller

"""Para crear un programa en ejecutable luego de haber instalado el pyinstaller, se busca la carpeta donde esta el archivo .py del programa y desde cmd ejecutamos
---Ejecutar
pyinstaller nombrearchivo.py
###ese comando generara varias carpetas una de ellas es la carpeta dist(distribucion) dentro de ella esta el archivo que se creo .exe mas sin embargo al ejecutarla
###sigue mostrando la terminal de cmd por detras por lo que hay que realizar pasos extras para eliminar dicha terminal 

---Ejecutar 
pyinstaller --windowed nombredearchivo.py 
###Este comando generara siempre las carpetas pero al ejecutar la aplicacion ya no saldra la terminal de cmd detras de la aplicacion


---Ejecutar
pyinstaller --windowed --onefile nombredearchivo.py 
###Pero para comprimir todo los archivos y hacer la aplicacion mas portable y que se pueda pasar a cualquier computadora y que se pueda ejecutar desde cualquiera es necesario agregar
###otro parametro 

-----Ejecutar
pyinstaller --windowed --onefile --ico=./logo.ico nombredearchivo.py 
###Existe un parametro extra que sirve para agregar una imagen de tipo icono a la aplicacion, la imagen debe tener extension .ico y debe estar en la misma 
ruta donde esta la aplicacion
"""