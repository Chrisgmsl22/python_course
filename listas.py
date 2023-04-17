#Profundizando en las listas
#Las listas son mutables

nombres = ['Carlos', 'Ricardo', 'Sergio']
apellidos = 'Magdaleno Gonzalez Acosta Martinez'.split()

#Sumar listas
print(f'Sumar listas: {nombres + apellidos}')

#Extender una lista con otra lista
nombres.extend(apellidos) #Agregamos los elementos de la lista 2
print(f'Extender la lista 1 con la lista 2: {nombres}')

#Lista de números
numeros = [10, 40, 15, 4, 20, 90, 4]
print(numeros)
#Obtener el índice del primer elemento encontrado en una lista
#help(list.index)
print(f'Indice 4: {numeros.index(4)}')

#Invertir el orden de una lista
numeros.reverse() #Invierte los elementos de una lista
print(f'Lista invertida: {numeros}')

#Ordenar los elementos de una lista de forma asc o desc
numeros.sort()
print(f'Lista ordenada: {numeros}')

#Ordena de manera descendente una lista
numeros.sort(reverse=True)
print(f'Lista descendente: {numeros}')


#Ontener el valor minimo y maximo de una lista
print(f'Valor mínimo: {min(numeros)}')
print(f'Valor máximo: {max(numeros)}')

#Copiar los elementos de una lista
numeros2 = numeros.copy()
print(numeros)
print(numeros2)
print(f'Misma referencia: {numeros is numeros2}')
print(f'Mismo contenido?: {numeros == numeros2}')

numeros2 = list(numeros)
print(f'Misma referencia: {numeros is numeros2}')
print(f'Mismo contenido?: {numeros == numeros2}')

#Slicing
numeros2 = numeros[:]
print(f'Misma referencia: {numeros is numeros2}')
print(f'Mismo contenido?: {numeros == numeros2}')

#Multiplicación de listas
lista_multiplicacion = 5*[[2, 5]]
print(lista_multiplicacion)
print(f'Misma referencia?: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido?: {lista_multiplicacion[0] == lista_multiplicacion[1]}')

#Matrices en python
print('Matrices'.center(50, '+'))
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(matriz)
print(f'Renglón 0 columna 0: {matriz[0][0]}')
print(f'Renglón 2, columna 2: {matriz[2][2]}')
print(f'Renglón 2, columna 3: {matriz[2][3]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

lista_de_listas = [[10, 14, 87, 90, 71], [4, 5, 6, 7], [9, 0, 11, 15, 45, 61, 70]]
lista_de_listas.sort(key=len)
print(f'Ordnear lista: {lista_de_listas}')

#Ordenamiento utilizando la función de sort, función built in
help(sorted)
nombres1 = ['Juan carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1) #Ordenamos de manera ascendente cada uno de los elementos
print(nombres1)

nombres1 = sorted(nombres1, reverse=True) #Ordenamos de manera ascendente cada uno de los elementos
print(nombres1)

#Ordenar por la cantidad de caracteres
nombres1 = sorted(nombres1, key=len)
print(nombres1)

#Built in de tipo reverse, podemos trabajar con cualquier iterable
nombres1 = reversed(nombres1)
print(list(nombres1))
