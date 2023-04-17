from Empleado import Empleado
from Gerente import Gerente

#Ejecutamos cualquiera de los metodos de str
def imprimirDetalles(obj):
    #print(obj) #De manera indirecta manda a llamar a str
    print(type(obj))#Tipo de clase al objeto en cual estamos apuntando
    if isinstance(obj, Gerente):
        obj.departamento
    print(obj.mostrarDetalles())

empleado = Empleado('Christian', 10000)
imprimirDetalles(empleado)

gerente = Gerente('Brenda', 6000, 'Seguros')
imprimirDetalles(gerente)

empleado.mostrarDetalles()
gerente.mostrarDetalles()

"""
    isInstante() pregunta si es una instancia de cierta clase
"""