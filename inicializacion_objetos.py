#Orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador padre')

    def mostrar_metodo(self):
        print('Método padre')

#definimos una clase que hereda de padre
class Hijo(Padre):
    #Se manda a llamar el metodo init de la clase padre siempre cuando el hijo
    #no define su propio metodo


    def __init__(self):
        super().__init__() #llamada a algun metodo del padre
        print('Inicializador hijo')

hijo = Hijo()
