#Para definir una clase personalizada para el manejo de excepciones
class NumerosIdenticosException(Exception):
    #Reciben un mensaje
    def __init__(self, mensaje):
        self.message = mensaje