class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self. apellido = apellido
        self.edad = edad

    #Sobreescribimos el metodo de +
    def __add__(self, other):
        return self.nombre + self.apellido + other.nombre + other.apellido

    def __sub__(self, other):
        return self.edad - other.edad

p1 = Persona('Kevin', 'Núñez', 33)
p2 = Persona('Ricardo', 'Fonseca', 10)

conca = p1 + p2
print(conca)

resta = p1 - p2
print(resta)