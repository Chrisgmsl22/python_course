#Es una funcion que encapsula otra funcion
#la funcion anidada puede acceder a las variables locales definidas en la funcion principal o ext

#Funcion principal
def operacion(a, b):
    #Definimos una funcion interna o anidada
    def sumar():
        return a + b

    #Retornamos la funcion
    return sumar

def operacion2(a, b):
    #1. Definimos una funcion lambda interna o anidada
    return lambda : a + b

mi_funcion_closure = operacion2(5, 2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')

#Llamar la funcion regresada al vuelo ()(), deben ser dos parentesis
print(f'Resultado de la funcion closure ejecutada al vuelo: {operacion2(2, 3)()}')