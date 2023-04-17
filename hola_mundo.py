#GUI - Graphical User Interface
#Tkiner - TK interface
import tkinter_ventanas as tk
#Importamos el módulo de componentes
from tkinter_ventanas import ttk

#Creamos un objeto usando la clase tk
ventana = tk.Tk()
#Modificamos el tamaño de la ventana
ventana.geometry('600x400')
#Cambiamos el nombre de la ventana
ventana.title('Nueva ventana')
#Configuramos el ícono de la aplicacion
ventana.iconbitmap('icono.ico')

#Definimos nuestro método evento click
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecución del evento_click')
    #Creamos un nuevo boton y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()#Para que se muestre el boton

#Creamos un boton ,
boton1 = ttk.Button(ventana, text='Aceptar', command=evento_click)#Lo incrustamos dentro de ventana


#Utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack() #INdicamos que se muestre dentro de la seccion indicada



#Iniciamos la ventana (esta linea se ejecuta al final)
#SI se ejecuta antes, no se muestran los cambios
ventana.mainloop()