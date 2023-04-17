import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

#configuramos el grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=10)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

#Definimos los eventos
def evento1():
    boton1.config(text='Boton 1 presionado')

def evento2():
    boton2.config(text='Boton 2 presionado')
def evento4():
    boton4.config(text='Boton 4 presionado')

#Definimos dos botones
boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton1.grid(row=0, column=0, sticky=tk.NSEW,
            padx=40, pady=30, ipadx=20, ipady=10,
            columnspan=2, rowspan=2)

#N, E, S W, NS, EW
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton2.grid(row=1, column=0, sticky=tk.NSEW)

boton3 = ttk.Button(ventana, text='Boton 3')
boton3.grid(row=0, column=1, sticky=tk.NSEW)

boton4 = ttk.Button(ventana, text='Boton 4', command=evento4)
boton4.grid(row=1, column=1, sticky=tk.NSEW)

ventana.mainloop()