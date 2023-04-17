from pprint import pprint as pp
#Profundizando en los diccionarios
#LLave->Valor

#Los diccionarios guardan un orden
diccionarioM = {'Nombre': 'Juan', 'Apellido':'Perez', 'Edad':'28'}
print(diccionarioM)

#Los diccionarios son mutables, pero las llaves deben de ser inmutables
#diccionario = {[1, 3]:'Valor'}
diccionario = {(1, 3):'Valor'}
print(diccionario)

#Si agregamos una llave si no se encuentra dentro del sdiccionario
diccionarioM['Departamento'] = 'Sistemas'

print(diccionarioM)

#No hay valores duplicados en las llaves de un diccionario, si ya existe, se reemplaza
diccionarioM['Nombre'] = 'Juan Carlos'
print(diccionarioM)

#Como recuperar elementos de un diccionario
#Recuperar un valor indicando una llave
print(diccionarioM['Nombre'])

#Si no encuentra la llave, lanza una excepcion
#Método get recupera una llave, si no existe, no lanza excepcion
#Podemos regresar un valor en caso de que no exista
print(diccionarioM.get('Nombre', 'No se encontró la llave'))
#

#SetDefault sí modifica el diccionario, además de que se agrega un valor por defecto
nombre = diccionarioM.setdefault('Nombre', 'Valor por default')


print(nombre)

#Imprimir con pprint
help(pp)
pp(diccionarioM) #Por defecto lo ordena de forma alfabética, para que no sea así ...
pp(diccionarioM, sort_dicts=False) #Agregamos este parámetro
