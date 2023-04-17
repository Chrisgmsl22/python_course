#Simulación de una sobrecarga de constructores en python
#Otras formas de crear objetos en python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None) #Manda a llamar de manera indirecta el constructor

    @classmethod
    def crear_persona_valores(cls, nombre=None, apellido=None):
        return cls(nombre=nombre, apellido=apellido)


persona1 = Persona('Juan', 'Perez')
persona_vacio = Persona.crear_persona_vacia()
persona_valores = Persona.crear_persona_valores(nombre='Karla', apellido='Gomez')

print(persona_vacio)
print(persona1)
print(persona_valores)