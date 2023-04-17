from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    #toString()
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'

    #Método de las clases
    def calcularArea(self):
        return self._alto * self._ancho


"""
    Para hacer uso de atributos que NO estan en esta clase, pero si en las
    heredadas, se manipulan con _guionBajo, self._atributoAjenoPeroHeredado
    
    No se puede instanciar una clase abstracta, para eso se crea otra
    clase que herede de la interfaz y así implementar todos sus métodS
    
    Se modifica el mro() ya que está de por medio una clase extra 
"""