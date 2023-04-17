import sys

from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import *


class Color(QWidget):
    def __init__(self, nuevo_color):
        super(Color, self).__init__()
        #indicamos que se puede agregar un color de fondo =
        self.setAutoFillBackground(True)
        paleta_colores = self.palette()
        #Creamos el componente de color de fondo aplicando el nuevo color
        paleta_colores.setColor(QPalette.Window, QColor(nuevo_color))
        #Aplicamos el nuevo color al componente
        self.setPalette(paleta_colores)

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Tabulador en PySide')
        #Creamos el componente de tab
        tabulador = QTabWidget()
        #Posicion de las etiquetas del tabulador
        tabulador.setTabPosition(QTabWidget.North)
        #Indicamos si queremos que se muevan las etiquetas del tabulador
        tabulador.setMovable(True)

        #agregamos los colores a cada tabulador
        tabulador.addTab(Color('red'), 'Rojo')
        tabulador.addTab(Color('yellow'), 'Amarillo')
        tabulador.addTab(Color('green'), 'Verde')

        self.setCentralWidget(tabulador)



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

#Con la notacion lambda pasamos un argumento

###
#
#
# #Anidar layouts(layout dentro de otro layout)
#         #Layout horizontal
#         layout_horizontal = QHBoxLayout()
#         layout_horizontal.setContentsMargins(5, 10, 5, 10)
#         #Agregamos un espacio entre cada elemento del layout horizontal
#         layout_horizontal.setSpacing(30)
#         layout_vertical = QVBoxLayout()
#         #Agregamos espacio en el layout vertical
#         layout_vertical.setContentsMargins(5, 10, 5, 10)
#         #Agregamos un espacio dentro de cada elemento del layout_vertical
#         layout_vertical.setSpacing(20)
#
#         #Agregamos algunos widgets al layout vertical
#         layout_vertical.addWidget(Color('green'))
#         layout_vertical.addWidget(Color('white'))
#         layout_vertical.addWidget(Color('red'))
#         #Agregamos el layout vertical dentro del layout_horizontal
#         #Se agrega de manera anidada
#         layout_horizontal.addLayout(layout_vertical)
#         #Agregamos mas elemenos al layout horixointal
#         layout_horizontal.addWidget(Color('yellow'))
#         layout_horizontal.addWidget(Color('purple'))
#         #Publicamos el layout (componente generico)
#           layout = QGridLayout()
#         layout.addWidget(Color('red'), 0, 0)
#         layout.addWidget(Color('blue'), 0, 2)
#         layout.addWidget(Color('green'), 1, 1)
#         layout.addWidget(Color('yellow'), 1, 0)
#         layout.addWidget(Color('purple'), 1, 2)
#
# ###