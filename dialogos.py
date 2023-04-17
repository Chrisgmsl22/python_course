import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Dialogos en PySide')
        #agregamos un boton
        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.click_boton)

        #Publicamos el boton
        self.setCentralWidget(boton)
    def click_boton(self, s):
        print(f'Click sobre boton { s}')
        #Creamos el dialogo personalizada
        dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta') #Ya tiene los botones yesNo

        if dialogo == QMessageBox.Yes:
            print('Regreso el valor de Yes')
        else:
            print('Regreso el valor de No')




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