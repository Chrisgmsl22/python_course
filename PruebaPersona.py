#Primero es el nombre del archivo, después el nombre de la clase, en este caso tienen el mismo nombre
from Persona import Persona

print(f'Creación de objetos'.center(50, '*'))
trabajador = Persona('Armando', 'Paredes', 21)
trabajador.saludar()

print(f'Eliminación de objetos'.center(50,'*'))
del trabajador

try:
   trabajador
except NameError:
    print('Ya no existe ')

print(__name__)


##Solo se agrega el atributo para este único objeto instanciado

#Métodos de instancia, método es una función, pero asociado a una clase. ctrl / comenta la linea

"""
    Si en los métodos no agregamos un @attribute.setter, entonces es un atributo de solo lectura
"""