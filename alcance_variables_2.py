#Más sobre funciones aniddadas y alcance de variables
def funcionExterna():
    variable_local_externa = 'Variable local externa'

    def funcion_anidada():
        variable_local_anidada = 'Variable local anidada'

        #Para usar una variable externa
        nonlocal variable_local_externa
        variable_local_externa = 'Nuevo valor local externo'
    funcion_anidada()

    print(f'Valor variable local externa: {variable_local_externa}')

funcionExterna()

#No es posible acceder a una variable local más interna
