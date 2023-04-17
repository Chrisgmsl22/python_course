#Este operador nos sirve para desempaquetar
numeros = [1, 2, 3]
print(numeros)

print(*numeros, sep=' - ')#Asterisco y luego el nombre de la lista

#En diccionarios se debe usar doble asterisco
def sumar(a, b, c):
    print(f'Resultado de la suma: {a + b + c}')
sumar(*numeros)

#Desempaquetando con variables
#Extraer algunas partes de una lista
mi_lista = list(range(1,7,1))
a, *b, c, d = mi_lista
print(a, b, c ,d)

#Se puede usar tammbién para unir listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [*lista1, *lista2]#Desempaquetamos tanto lista 1 como lista 2

print(lista3)

#Unir diccionarios
dic = {'A':'1', 'B':'2', 'C':'3'}
dic2 = {'D':'4', 'E':'5'}
dic3 = {**dic, **dic2} #Desempaquetamos ambos diccionarios

print(dic3)

#Cómo construir una lista a partir de un string
lista = [*'Hola Mundo']
print(lista)
print(*lista)

#Zip permite unir uno o mas iterables