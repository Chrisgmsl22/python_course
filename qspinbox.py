import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *


class Componentes(QMainWindow):
    def __init__(self):
        super(Componentes, self).__init__()
        self.setWindowTitle('Componentes')
        #QSlider es para valores numericos enteros en un slider(deslizador)
        #QDial es una rueda, utilizada para aplicaciones de audio
        componente = QDial()
        componente.setMinimum(-5)
        componente.setMaximum(8)

        #conectamos a las señales
        componente.valueChanged.connect(self.cambio_valor)
        componente.sliderMoved.connect(self.slider_cambio_posicion)
        componente.sliderPressed.connect(self.slider_presionado)
        componente.sliderReleased.connect(self.slider_liberado)

        # Publicamos este componente
        self.setCentralWidget(componente)
    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')
    def slider_cambio_posicion(self, nueva_posicion):
        print(f'Nueva posicion: {nueva_posicion}')
    def slider_presionado(self):
        print(f'Dial preionado')
    def slider_liberado(self):
        print('Dial liberado')



if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
##
# self.setFixedSize(500, 600)
#         #Creamos un componente de tipo etiqueta
#         etiqueta = QLabel('Hola')
#         etiqueta.setPixmap(QPixmap('layla.jpg'))
#         etiqueta.setScaledContents(True)
# d

#
#
# #
### self.setFixedSize(500, 600)
# Creamos un componente de tipo etiqueta
# etiqueta = QLabel('Hola')
# etiqueta.setPixmap(QPixmap('layla.jpg'))
# etiqueta.setScaledContents(True)


# #modificamos el estado inicial
#         etiqueta.setText('Saludos') #setText nos permite modificar el valor que tiene nuestra etiqueta
#         #modificamos la fuente
#         fuente = etiqueta.font()
#         fuente.setPointSize(25)
#         etiqueta.setFont(fuente)
#         #Modificamos la alineacion de la etiqueta
#         etiqueta.setAlignment(Qt.AlignCenter)


# ###
# J´B