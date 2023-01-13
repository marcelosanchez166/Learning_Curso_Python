import PyPDF2

# Cargamos el documento PDF con los permisos de lectura.

pdfFileobj = open('archivo.pdf', 'rb')

# Abrimos el documento PDF usando PyPDF2.

pdfReader = PyPDF2.PdfFileReader(pdfFileobj)

# Podemos acceder a informacion general del documento, como: numero de paginas O si esta encriptado.
print ("Cantidad de paginas: ", pdfReader.numPages)
print("Encriptado: ", pdfReader.isEncrypted)

# Tambien podemos obtener un diccionario con informacion mas detallada del documento.
info = pdfReader.documentInfo

print ("Fecha de creacion", info.get('/creationDate'))
print("Fecha de modificacion", info.get('/HodDate'))
print("Creador", info.get('/Creator'))

# Para leer el contenido del PDF es necesario indicar la pagina objetivo y extraer el texto.
pageobj = pdfReader.getPage (0)
print (pageobj.extractText ())
# Si quieres extraer todo el texto del PDF puedes usar un ciclo for.
for x in range(0, pdfReader.numPages):
    pageObj = pdfReader.getPage (x)
    print(pageObj.extractText())

