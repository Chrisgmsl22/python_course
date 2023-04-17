#Leer contenido online


# Leer contenido online
import urllib
from urllib.request import urlopen

# Debido a cambios en la libreria se deben hacer los siguientes cambios:
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
    # contenido = mensaje.read()
    palabras = []
    for linea in mensaje:
        palabras_por_linea = linea.decode('UTF-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra) #Metemos cada palabra en el listado
print(palabras)

#with open('nuevo_archivo.txt','w', encoding='utf-8') as archivo:
#    archivo.write(contenido)
with urlopen(peticion) as mensaje:
    # contenido = mensaje.read()
    contenido = mensaje.read().decode('UTF-8')
print(contenido.count('Universidad'))

print(contenido.upper())
print(contenido)

#Lower, convierte a minusculas una cadena
print(contenido.lower())
#Buscamos la cadena python
print('Python' in contenido)

#starts with, inicia con
print(contenido.startswith('En GlobalMentoring.com.mx'))
#endswith, termina con
print(contenido.endswith('GlobalMentoring.com.mx'))

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())
print(mensaje.upper().isupper())

print('Alineando cadenas'.center(50, '+'))

titulo = 'Sitio Web de GlobalMentoring.com.mx'
print(len(titulo))
print(titulo)

#Cómo alinea un texto hacia la izquierda
print(titulo.ljust(50, '+'))
print(titulo.rjust(50, '-'))

#Método replace, reemplaza contenido en un string
print(contenido.replace(' ', '-'))


#Eliminar caracteres al inicio y final de una cadena
print('Método strip'.center(50, '+'))
titulo = ' *** GlobalMentoring.com.mx *** '
print(f'Cadena original: {titulo}, {len(titulo)}')
titulo = titulo.strip() #Quita espacios en blanco al inicio y al final
print(f'Cadena modificada: {titulo}, {len(titulo)}')
titulo = '***GlobalBaby***'
titulo.strip('*')
print(f'Cadena modificada: {titulo.strip()}')

titulo = '+++GlobalBaby+++'.lstrip('+')
print(titulo)

titulo = ' *** GlobalMentoring.com.mx *** '.strip().strip('*').strip()
print(titulo)
