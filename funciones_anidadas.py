#Profundizando funciones anidadas
def calculadora(a, b):
    #Primer función anidada
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    #Llamamos a la función anidada
    print(f'Resultado de sumar: {sumar(a, b)}')
    print(f'Resultado de restar: {restar(a, b)}')

#Primero se define la función, después se manda a llamar
calculadora(5, 6)