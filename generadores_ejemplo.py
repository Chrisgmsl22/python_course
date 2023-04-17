#Definimos un primer generador del 1 al 5
def generador_numeros():
    for numero in range(1, 5, 1):
        yield numero #Por cada numero del rango, producimos su valor
        print('Se reanuda la ejecución de la función')

#Utilizamos el objeto generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador)) #Es de clase generator

#Consumimos los valores del generador
for valor in generador:
    print(f'Número producido: {valor}')