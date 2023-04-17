from Producto import  Producto
from Orden import Orden


camisa = Producto('Camisa', 60)
short = Producto('Short', 55)
calcetines = Producto('Calcetines', 50.00)
blusa = Producto('Blusa', 12)

    #Creamos una lista de productos
productos = [camisa, short]
productos2 = [calcetines, blusa] #Segunda lista de productos
#Creamos una orden
ordenUno = Orden(productos)
ordenDos = Orden(productos2) #Segunda losta de productos

#Agregamos mas productos a la orden uno
ordenUno.agregarProducto(productos2)

print(ordenUno)
print(f'El total de la orden uno: {ordenUno.calcularTotal()}')
print(ordenDos)
print(f'El total de la orden dos es: {ordenDos.calcularTotal()}')
