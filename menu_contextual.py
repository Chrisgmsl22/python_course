import sys
from random import randint

import PySide6
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *




class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Menu contextual')
        #Sobreescribimos el metodo del menu contextual
        # Y mostramos
        self.show()
        #Nos conectamos a la señal de custom context menu requested
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        menu_contextual = QMenu(self)
        #Definimos los botones
        boton_nuevo = QAction(QIcon('nuevo.png') ,'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png') ,'Guardar', self)
        boton_salir = QAction('Salir', self)

        # Asociamos el evento click (nos conectamos a traves de triggered)
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_salir.triggered.connect(self.click_boton_salir)

        #Podemos agregar acciones
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        #Recuperamos la posicion del cursor como posicion global de la ventana padre
        #Y ejecutamos menu contectual
        menu_contextual.exec(self.mapToGlobal(pos)) #Posicion global donde se dio click derecho

    def click_boton_nuevo(self, status):
        print(f'Nuevo archivo {status}')
    def click_boton_guardar(self, s):
        print(f'Guardar: {s}')
    def click_boton_salir(self, s):
        #print(f'Acerca de: {s}')
        sys.exit()






if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())

#Con la notacion lambda pasamos un argumento

