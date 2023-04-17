from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    #Obligatorio indicar el tipo de dato
    calle: str
    numero: int

@dataclass(eq=True, frozen=True)
class Persona:
    #Tenemos que indicar que es una clase de tipo DataClass
    nombre: str
    apellido: str
    domiclio: Domicilio

    #Atributos de clase
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        #validaciones van aqui
        if not self.nombre:
            raise ValueError(f'Valor de nombre vacío: {self.nombre}')

domicilio1 = Domicilio('Neptuno', 33)

persona1 = Persona('Juan', 'Perez', domicilio1)
print(persona1)

#Variables de clase
print(f'Variable de clase: {persona1.contador_personas}')
#Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
#Variable con valores vacíos
persona_vacia = Persona('Hector', 'Sanchez', domicilio1)
print(persona_vacia)
#Revisar igualdad entre objetos
persona2 = Persona('Carlos', 'Madariaga', domicilio1)
print(f'Objetos iguales?: {persona1 == persona2}')
#Agregar esta clase a una coleccion
coleccion = {persona1, persona2} #al ser mutables, no pueden ser parte de un set
print(coleccion)
#El atributo frozen dentro del decorador nos permite mutar o inmutar a los atributos de un objeto