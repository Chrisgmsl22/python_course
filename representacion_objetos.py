#tres formas que existen para representar objetos
#Representación de objetos (str, repr, format)

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #repr, más enfocado a los programadores
    def __repr__(self):
        return f'Persona(nombre:{self.nombre}, apellido:{self.apellido})'

    #str, más enfocado al usuario final
    #La implementación por defaault llama al metodo rep
    def __str__(self):
        return f'nombre: {self.nombre}, apellido: {self.apellido}'

    #format
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre} y apellido {self.apellido}'

persona1 = Persona('Juean', 'Carlo')
#Método repr
print(persona1.__repr__())

#método str
print(persona1)

#método format, se llama si se encuentra dentro de un f string
print(f'{persona1}')