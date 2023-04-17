class Aritmetica:
    """
    CLase Aritmética para realizar las operaciones de sumar, restar, multiplicar
    dividir
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    #Definición de los metodos de la clase
    def sumar(self) -> int:
        return self.operandoA + self.operandoB
    def restar(self):
        return self.operandoA - self.operandoB
    def multiplicar(self):
        return self.operandoA * self.operandoB
    def dividir(self):
        return self.operandoA / self.operandoB

#Instanciamos objetos
aritmeticos = Aritmetica(3, 3)

print(f'{aritmeticos.sumar()}')
print(aritmeticos.restar())
print(aritmeticos.multiplicar())
print(aritmeticos.dividir())