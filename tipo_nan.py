import math
from decimal import Decimal

# NaN - Not a Number
# NaN - No es case sentitive
# NaN - Es un tipo de dato númerico indefinido
variable = float('NaN')
print(f'variable: {variable}')
print(f'Es NaN?: {math.isnan(variable)}')

variable = Decimal('NaN')
print(f'variable: {variable}')
print(f'Es NaN?: {math.isnan(variable)}')


