#Para convertir una clase, en una clase abstracta
#se tiene que extender de ABC = Abstract Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        #Indicamos los valores dentro del constructor
        #Validación
        if self._validarValor(ancho):
           self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo: {ancho}')

        if self._validarValor(alto):
            self._alto = alto
            print(f'Valor erróneo: {alto}')
        else:
            self._alto = 0

        #Método toString()
    def __str__(self):
        return f'ancho: {self._ancho}, alto: {self._alto}'

    #Getters y setters
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        if self._validarValor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erróneo: {ancho}')

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        if self._validarValor(alto):
            self._alto = alto
        else:
            print(f'Valor erróneo: {alto}')
    #Método encapsulado
    def _validarValor(self, valor):
        #Validación simplificada
        return True if 0 < valor < 10 else False

    #Método abstracto (interfaces) que no tienen implementacion
    @abstractmethod
    def calcularArea(self):
        pass #Solo se usa para definir estructura