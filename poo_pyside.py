import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPyside(QMainWindow):
    def __init__(self):
        #llamamos al init de la clase padre
        super().__init__()
        self.setWindowTitle('POO con PySide')
        #self.resize(600, 400)
        self.setFixedSize(QSize(600, 400))
        self._agregar_componentes()

    def _agregar_componentes(self):
        #Agregamos algunos componentes
        #Agregamos un menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        #Agregamos algunas opciones al menu
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        #Agregamos un texto en la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        #Agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Información de la barra de estado...')
        #Agregamos un componente de boton
        boton = QPushButton('Nuevo boton')
        #Publicamos el boton en la ventana
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication(sys.argv) #Podemos pasar argumentos vacios
    ventana1 = VentanaPyside()
    ventana1.show()

    #Ejecutamos la ventana
    sys.exit(app.exec())