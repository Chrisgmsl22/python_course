from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creación objeto cuadrado'.center(50,'+'))

cuadrado = Cuadrado(5, 'Rojo')

print('Creación objeto rectángulo'.center(5,'+'))
rectangulo = Rectangulo(6, 5, 'Azul')

print(f'{cuadrado.calcularArea()}, {cuadrado.__str__()}')
print(Cuadrado.mro())

print(f'{rectangulo.calcularArea()}, {rectangulo.__str__()}')
print(Rectangulo.mro())
"""
    Con herencia multiple, es importante tener el orden en erl que se llaman
    las clases padre, para eso existe el metodo MRO Method Resolution Order
"""