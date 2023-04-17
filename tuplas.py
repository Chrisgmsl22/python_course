#Profundizando tuplas
#Tuplas son inmutables
#Declarar variables
a, b = 'Hola', 'Adios'
print(a, b)

#Swap
a, b = b, a
print(a,b)

#Regresamos multiples valores
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax(range(1, 6, 1))
print(min, max)

#Regresar la suma de una tupla
resultado = sum(range(1,6,1))
print(resultado)

def sumar(*args):
    return sum(args)

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)