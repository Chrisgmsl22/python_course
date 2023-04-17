#Son los lugares donde podemos usar una variable
#Sope
variable_global = 'Variable global'

def imprimir():
    #Para acceder a una variable global
    #Indicamos que vamos a trabajar con una variable global
    global variable_global
    print(f'Variable global accedida desde una función: {variable_global}')
    #Definición de una variable local
    variable_local = 'Variable local'
    print(f'Variable local accedida desde la función: {variable_local}')
    variable_global = 'Nuevo valor del global'
    def funcionAnidada():
        print(f'Variable local dentro de la función anidada: {variable_local}')

    funcionAnidada()

imprimir()
print(f'Variable global fuera de la función: {variable_global}')
#No es posible acceder a variables locales fuera del bloque donde se definieron