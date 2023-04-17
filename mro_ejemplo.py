class Clase1:
    #esta es la clase padre
    def __init__(self):
        print('Clase1.__init__')
    def metodo(self):
        print('Metodo clase1')

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
    def metodo(self):
        print('Metodo clase2')
        super().metodo()

class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
    def metodo(self):
        print('Método clase3')
        super().metodo()

class Clase4(Clase2, Clase3):
    #No hay init aqui
    def metodo(self):
        print('Método clase4')
        super().metodo()

#Creamos un objeto de la clase 4
clase4 = Clase4()
# __bases__, nos muestra las clases que hereda de manera directa
print(Clase4.__bases__)
print(Clase4.mro())

#cuál método se ejecuta?
clase4.metodo()
