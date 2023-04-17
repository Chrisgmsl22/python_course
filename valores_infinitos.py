import math
from decimal import Decimal

#Manejo de valores infinitos
infinitoPositivo = float('inf')
print(f'Infinito Positivo: {infinitoPositivo}')
#Preguntamos si un valor es infinito
print(f'Es infinito: {math.isinf(infinitoPositivo)}')

infinitoNegativo = float('-inf')
print(f'Infinito Negativo: {infinitoNegativo}')
#Preguntamos si el valor es infinito
print(f'Es infinito: {math.isinf(infinitoNegativo)}')


print('Leccion Nueva'.center(50, '*'))
infinitoPositivo = math.inf
print(f'Infinito Positivo: {infinitoPositivo}')
#Preguntamos si un valor es infinito
print(f'Es infinito: {math.isinf(infinitoPositivo)}')

infinitoNegativo = -math.inf
print(f'Infinito Negativo: {infinitoNegativo}')
#Preguntamos si un valor es infinito
print(f'Es infinito: {math.isinf(infinitoNegativo)}')


print('Modulo decimal'.center(50, '+'))
infinitoPositivo = Decimal('Infinity')
print(f'Infinito Positivo: {infinitoPositivo}')
#Preguntamos si un valor es infinito
print(f'Es infinito: {math.isinf(infinitoPositivo)}')

infinitoNegativo = Decimal('-Infinity')
print(f'Infinito Negativo: {infinitoNegativo}')
#Preguntamos si un valor es infinito
print(f'Es infinito: {math.isinf(infinitoNegativo)}')