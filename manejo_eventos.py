#Signals y slotys
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Signals y Slots')

        self.boton = QPushButton('Click Aquí')
        #Conectamos el evento signal con el slot evento_click

        #Asociamos la señal de click al slot evento_click
        self.boton.clicked.connect(self.evento_click)
        #Conectar ala señal del cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)

        #Publicamos el boton
        self.setCentralWidget(self.boton)

    def evento_click(self):
        #Cambiaar el texto del boton y el titulo de la ventana
        self.boton.setText('Nuevo Texto')
        self.boton.setEnabled(False)#no podemos interactuar con el boton
        self.setWindowTitle('Nuevo titulo')
        print('Evento click')

    def cambio_titulo_aplicacion(self, nuevo_titulo):
        print(f'Nuevo titulo aplicación: {nuevo_titulo}')

    def evento_checar(self, checar):
        self.boton_checado = checar
        print('Checado?', checar)


if __name__ == '__main__':
    #Creamos un objeto de aplcacion
    app = QApplication([])
    #Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())


#
#
#
#