from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    #toString()
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

    #Metodop de esta clase
    def calcularArea(self):
        return f'El área es: {self._ancho * self._alto}'


"""
    Cuando mandamos a llamar al inicializadoe de la clase padre, se debe acceder
    por medio del nombre de la clase, seguido del método init, y como argumento
    debemos pasar self, ya que se hacen uso de algunas variables dentro de la
    declaración de la clase
"""