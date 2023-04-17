class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

#Mostrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__) #Despliega los atributos asosiados al objeto

#Crear un atributo al vuelo
print(persona1.contador_personas) #Atributo de objeto
#Pero no es posible modificarrlo con el objeto, sino con la clase
persona1.contador_personas = 10
print(persona1.__dict__)

#El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) #Atributo de clase

persona2 = Persona('Brenda', 'Zarni')
print(persona2.__dict__)
print(persona2.contador_personas)