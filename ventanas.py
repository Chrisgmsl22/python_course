import sys
from random import randint

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *

#Cualquier componente nos sirve
class NuevaVentana(QWidget):
    def __init__(self):
        super(NuevaVentana, self).__init__()
        self.setWindowTitle('Nueva Ventana')
        layout = QVBoxLayout()
        self.etiqueta = QLabel(f'Nueva Ventana: {randint(0, 100)}')
        layout.addWidget(self.etiqueta)
        self.setLayout(layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.nueva_ventana = NuevaVentana() # Valor por default, creamos la ventana
        self.setWindowTitle('Ventanas en PySide')
        self.boton = QPushButton('Mostrar / Ocultar ventana')
        self.boton.clicked.connect(self.mostrar_nueva_ventana)

        # Definimos una entrada de texto
        self.entada_texto = QLineEdit()
        self.entada_texto.textChanged.connect(self.nueva_ventana.etiqueta.setText) #cualquier cambio en la entrada de texto
        # se la pasamos a la nueva ventana
        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.boton)
        layout.addWidget(self.entada_texto) # para poder capturar informacion

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_nueva_ventana(self, s):
        if self.nueva_ventana.isVisible():
            # Entonces la ocultamos (solo tenemos una instancia)
            self.nueva_ventana.hide()
        else:
            self.nueva_ventana.show()

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

#Con la notacion lambda pasamos un argumento

