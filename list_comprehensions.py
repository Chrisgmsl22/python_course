#Es un tipo de listas
#Primero creamos una lista
numeros = range(1, 10, 1)
lista_pares = []

#Creamos una nueva lista con los valores pares
for numero in numeros:
    #Revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista de pares: {lista_pares}')

#Hacemos lo mismo, pero con list comprehensions
#[expresion] for var in coleccion if condicion
#La condición del if es opcional
lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]

print(f'Lista pares: {lista_pares}')

#EJemplo similas pero con dos condiciones
#Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
#Es decir, se debe dividir entre dos y divisible entre 6
pares = [numero for numero in range(50) if numero % 2 == 0 if numero % 6 == 0]
print(f'Lista divisible entre 2 y entre 6: {pares}')

#Agregando if else
lista_pares = []
lista_impares = []

for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

#Ahora con list comprehensions
lista_pares = []
lista_impares = []

#Primero van las expresiones, lueggo las condiciones, luego lo que se quiere hacerr
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero)
 for numero in range(10)]

print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

#lista de listas y convertirlo a una lista simple
lista_listas = [[1, 2, 3], [4, 5 ,6], [7, 8 ,9, 10]] #Tenemos tres sublistas

#Convertimos la lista de listas en una sola lista
#Creamos nuestra list comprehension
#La expresión es el valor que se va a retornar
lista_simple = [valor
                for sublista in lista_listas
                for valor in sublista]
print(f'Lista simple: {lista_simple}')

#Ahora creamos una lista de numeros pares a partir de la lista de listas
#sin list comprehensions, ciclos for anidados
lista_pares = []
for sublista in lista_listas:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)
print(f'Lista pares: {lista_pares}')

#ahora el mismo ejercicio con list comprehensions
#no es necesario separar las lineas, solo es para mejor lectura del codigo
lista_pares = []
lista_pares = [valor
               for sublista in lista_listas
               for valor in sublista if valor % 2 == 0]
print(f'Lista pares con list comprehension: {lista_pares}')