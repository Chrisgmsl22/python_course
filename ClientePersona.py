from Empleado import Empleado
from Persona import Persona

print('Iniciando las pruebas'.center(50, '+'))

#Instanciamos los objetos
persona = Persona('Julio', 'Patán', 20)
print(persona)
empleado = Empleado(8000,'Martin', 'Lutero', 44)
print(empleado)


empleado.saludar()

