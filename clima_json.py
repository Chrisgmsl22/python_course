# ESTA RESPUESTA ES PARA EL EJERCICIO DE PERSONAS, ESPERO Y LES FUNCIONE
import json
from urllib.request import Request, urlopen

url = Request('http://globalmentoring.com.mx/api/clima.json')  # Hacemos el request para la URL
url.add_header('User-Agent',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')  # Pasamos el header
respuesta = urlopen(url)  # Abrimos lo que hay en la URL
print(respuesta)

#Recuperamos el cuerpo de la respuesta
cuerpo_respuesta = respuesta.read()

# Procesamiento de respuesta (quitamos origen binario)
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

# imprimir solo los nombres de las personas
# JSON se convierte a listas y diccionarios en python
print(json_respuesta['clima'])

#1. Acceder a la descripción del clima
descripcion_clima = json_respuesta['clima'][0]['descripcion'] #Recuperamos solo el primer objeto
print(f'Descripción del clima: {descripcion_clima}')

#2. Mostrar la temperatura mínima y máxima
temp_min = json_respuesta['principal']['temp_min']
print(f'La temperatura mínima es: {temp_min} grados')
temp_max = json_respuesta['principal']['temp_max']
print(f'La temperatura máxima es: {temp_max} grados')

