#Signals y slotys
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400, 200)
        #Definimos la etiqueta y linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        #Conectar el widget de entrada de texto con la etiqueta
        #la señal es textChanged, y el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        #publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        #creamos un contenedor para ubicar el layout
        contenedor = QWidget()
        contenedor.setLayout(disposicion)

        #publicamos el contenedor, el cual ya incluye los demas elementos
        self.setCentralWidget(contenedor)




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