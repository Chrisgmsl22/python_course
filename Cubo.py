class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    #Métodos dentro de la clase
    def calcularVolumen(self):
        return self.ancho * self.profundo * self.alto

#función fuera de la clase
def calcularVolumenCubo(cubo: Cubo):
    print(f'El volumen del cubo es: {cubo.calcularVolumen()}m cúbicos')

#Obtenemos los valores de forma individual
ancho = int(input('Ingresa el ancho: '))
profundo = int(input('Ingresa el profundo: '))
alto = int(input('Ingresa el alto: '))

cuboObj = Cubo(ancho, profundo, alto)

#Llamamos a la función que hace llamada al método el ibjeto
calcularVolumenCubo(cuboObj)