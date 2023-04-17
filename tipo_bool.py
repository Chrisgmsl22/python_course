# bool : Boolean, contiene True y False
#Tipos numéricos. False para 0 y True para demás valores
valor = 0
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 1
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

print('Nueva lección'.center(50, '*'))

#Tipo str, False para '', True demás valores
valor = ""
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = "full"
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')


print('Listas'.center(50, '*'))
#Para tipo colecciones, Falso colecciones vacias y verdadero para las demás colecciones
valor = []
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = [1, 2]
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')


print('Tuplas'.center(50, '+'))
#Ahora con tuplas
valor = ()
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = (1, 2, 3)
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')


print('Diccionario'.center(50, '+'))
#COn un diccionario
valor = ()
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')


valor = {1: 'John', 2: 'Fernando'}
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

print('Sentencias de control'.center(50, '+'))
#Usando sentencias de control
if 11:
    print('Regresó verdadero')
else:
    print('Regreso falso')

variable = [1, 2]
while variable:
    print('Ejecución ciclo while')
    break
else:
    print('Regresó falso')