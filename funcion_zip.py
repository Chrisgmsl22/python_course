print(dir(__builtins__))

#Zip usara la coleccion con el menor número de elementos
numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
identificadores = 321, 322, 333, 324, 325


conjunto = {6, 4, 0, 9, 8, 15, 10 }
#Unir esos dos elementos en un solo iterable
mezcla = zip(numeros, letras, identificadores, conjunto)
print(mezcla)
print(list(mezcla))

print(type(mezcla))

#Iterar en paralelo
for numero, letra, identificador, aleatorio in zip(numeros, letras, identificadores, conjunto):
    print(f'Número: {numero}, Letra: {letra}, id: {identificador}, Aleatorio: {aleatorio}')

nueva_lista = []
for numero, letra, identificador, aleatorio in zip(numeros, letras, identificadores, conjunto):
    #print(f'Número: {numero}, Letra: {letra}, id: {identificador}, Aleatorio: {aleatorio}')
    nueva_lista.append(f'{identificador}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)

#Artificial función unzip
mezcla = [1, 'a',(2, 'b'), (3, 'c')]
#El objetivo es realizar el proceso inverso
#numeros, letras = zip(*mezcla)
#Primero hacemos unpacking de los elementos

print(f'Números: {numeros}, Letras: {letras}')

letras = ['c', 'd', 'a', 'e', 'b']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
#Sin ordenamiento
print(tuple(mezcla))
print(sorted(zip(letras, numeros)))

#Cómo crear un diccionario a partir de dos iterables
#Primero creamos un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]

#Creamos un diccionario
diccionario = dict(zip(llaves, valores))
print(diccionario)

#Actualizar un elemento del diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)