import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

#Clase base de Qt (PySide)
#e encarga de procesar los eventos (event loop)

app = QApplication()
#Crear un objeto ventana (cualquier componente puede ser una ventana)
#ventana = QPushButton('Boton de PySide')
ventana = QMainWindow()
#Cambiamos el titulo
ventana.setWindowTitle('Hola Mundo con Pyside')
#Tamaño de la ventana
ventana.resize(600, 400)

#Mostramos la ventana
ventana.show()


#Se ejecuta la aplicación
sys.exit(app.exec())
