base =float(input('Introduce la base imponible de la factura: '))

def aplica_iva(base, iva = 21):
          base += base * iva  /100
          return base 
print(aplica_iva(base))