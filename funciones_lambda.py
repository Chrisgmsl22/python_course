#Una función lambda son funciones anonimas
#Son pequeñas, una linea de codigo

def sumar(a, b):
    return a + b

#Con una función lambda, la función es anonima
#No se necesita agregar paréntesis para los parámetros
#No se necesita usar la palabra return, pero sí debe regresar una expresión valida]
mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4, 6)
print(resultado)

#Funcion lambda que no recibe argumentos, pero si debemos de regresar una funcion válida
mi_funcion_lambda = lambda : 'Función sibn argumentos'
print(f'Llamar función lambda sin argumentos: {mi_funcion_lambda()}')

#Funcion lambda con parametros por default
mi_funcion_lambda = lambda a = 2, b = 3 : a + b
print(f'Resultado de argumentos por default: {mi_funcion_lambda()}')

#Funcion con argumentos variables k**args
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)

print(f'Resultado de argumentos variables: {mi_funcion_lambda(1, 2, 3, a=5, b=6)}')

#Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)

print(f'Resultado de la funcion lambda: {mi_funcion_lambda(1, 2 ,4, 5, 6, 7, e=5, f=7)}')

