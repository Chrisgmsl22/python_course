class Producto:
    #Variables de clase
    contadorProductos = 0

    #Método constructor
    def __init__(self, nombre, precio):
        #Incrementamos en uno el contador del objeto
        self._idProducto = Producto.incrementarContador() #Lo asignamos a una variable
        self._nombre = nombre
        self._precio = precio

    @classmethod
    def incrementarContador(cls):
        cls.contadorProductos += 1
        return cls.contadorProductos

    #Getter de precio
    @property
    def precio(self):
        return self._precio #Sí se retorna el valor encapsulado

    #Método toString()
    def __str__(self):
        return f'[id: {self._idProducto}, name: {self._nombre}, ${self._precio}]'

if __name__ == '__main__':
    producto1 = Producto('T-Shirt', 60)
    print(producto1)
    producto2 = Producto('Shorts', 100)
    print(producto2)
else:
    print('Valor erróneo')