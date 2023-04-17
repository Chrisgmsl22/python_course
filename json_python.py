# ESTA RESPUESTA ES PARA EL EJERCICIO DE PERSONAS, ESPERO Y LES FUNCIONE
import json
from urllib.request import Request, urlopen

url = Request('http://globalmentoring.com.mx/api/personas.json')  # Hacemos el request para la URL
url.add_header('User-Agent',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')  # Pasamos el header
respuesta = urlopen(url)  # Abrimos lo que hay en la URL
print(respuesta)

cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)
# Procesamiento de respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

# imprimir solo los nombres de las personas
# JSON se convierte a listas y diccionarios en python

for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')