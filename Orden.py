from Computadora import Computadora

class Orden:
    #Variables de clase (estáticas)
    contadorOrdenes: int = 0

    def __init__(self, computadoras: list):
        self._idOrden = Orden.incrementarContador()
        self._computadoras = computadoras

    def agregarComputadora(self, computadora: Computadora):
        #Creamos una lista de tipo computadra
        self._computadoras.append(computadora)
        print(f'Computadora Agregada'.center(50, '+'))


    @classmethod
    def incrementarContador(cls):
        cls.contadorOrdenes = cls.contadorOrdenes + 1
        return cls.contadorOrdenes

    def __str__(self):

        computadorasStr = ''
        for computadora in self._computadoras:
            computadorasStr += computadora.__str__()

        return f'''
            Orden: {self._idOrden}
            Computadoras: {computadorasStr}
        '''

if __name__ == '__main__':
    #Creamos objetos
    monitorObj = Monitor('Asus', 32)
    tecladoObj = Teclado('Usb', 'Glorious')
    ratonObj = Raton('Bluetooth', 'Logitech')
    computadoraObj = Computadora('PC Gamer', monitorObj, tecladoObj, ratonObj)

    ordenObj = Orden()
    ordenObj.agregarComputadora(computadoraObj)
    print(ordenObj)