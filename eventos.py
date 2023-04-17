import sys
from random import randint

import PySide6
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *




class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Eventos')
        # Capturar eventos con el mouse
        self.etiqueta=QLabel('Da click en esta ventana ')
        self.setCentralWidget(self.etiqueta)



    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent):
        self.etiqueta.setText('Evento mousePressedEvent detectado')
        #Preguntamos por el boton del mouse que lanzo el evento
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('mousePressedEvent Boton izquierdo')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mousePressedEvent Boton Central')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mousePressedEvent Boton Derecho')

    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('Evento mouseReleasedEvent Boton Izquierdo')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mouseReleasedEvent Boton Derecho')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseReleasedEvent Boton Medio')
    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent):
        #self.etiqueta.setText('Evento mouseDoubleClickEvent detectado')
        if event.button() == Qt.LeftButton:
            self.etiqueta.setText('Evento mouseDoubleClickEvent Boton Izquierdo')
        elif event.button() == Qt.RightButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton Derecho')
        elif event.button() == Qt.MiddleButton:
            self.etiqueta.setText('mouseDoubleClickEvent Boton Medio')



if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

#Con la notacion lambda pasamos un argumento

