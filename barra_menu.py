import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import *
from PySide6.QtWidgets import *



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Barra de Herramientas en PySide')
        #Publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        #Creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16, 16))
        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle) #barra de herramientas se acopla al sistema operativo
        barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(barra)

        #Agregamos un elemento a nuestra barra de herramientas (seran los elementos)
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        #Agregamos el boton a la barra
        barra.addAction(boton_nuevo) #Agregar un elemento con clase action
        barra.addAction(boton_guardar)

        #Barra de estado, mostramos
        self.setStatusBar(QStatusBar(self))

        #Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo archivo')
        boton_guardar.setStatusTip('Guardar Archivo')

        #Asociamos el evento click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.click_boton_guardar)

        barra.addSeparator() #Agregamos un separador en la barra
        barra.addWidget(QCheckBox())

        #Hacemos checable el boton
        #boton_nuevo.setCheckable(True)

        #menus
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        menu_archivo.addAction(boton_nuevo)

        #Agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)

        #Agregamos un separador
        menu_archivo.addSeparator()

        #agregamos una tercera opcion
        boton_salir = QAction('Salir', self) #Self es cuando le asignamos el objeto padre
        menu_archivo.addAction(boton_salir)

        #Submenu ayuda
        boton_acerca_de = QAction(QIcon('acerca.png'), 'Acerca de', self) #Self es cuando le asignamos el objeto padre
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca_de)

        boton_acerca_de.triggered.connect(self.click_boton_acerca_de)

        #agregamos submenu dentro del submenu
        menu_archivo.addMenu(menu_ayuda)

        #Creacion de atajos para nuestro menu
        #COmbinacion de teclas
        boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        boton_acerca_de.setShortcut(QKeySequence('Ctrl+a'))
        boton_guardar.setShortcut(QKeySequence('Ctrl+g'))

    def click_boton_nuevo(self, status):
        print(f'Nuevo archivo {status}')
    def click_boton_guardar(self, s):
        print(f'Guardar: {s}')
    def click_boton_acerca_de(self, s):
        print(f'Acerca de: {s}')



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