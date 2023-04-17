import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Componentes')
ventana.iconbitmap('icono.ico')

#Width hace referencia a la cantidad de caracteres de entrada
# state deshabilita el componente



entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)
#Texto de ayuda al inicio
entrada1.insert(0, 'Introduce una cadena')
entrada1.insert(tk.END, '...')
#entrada1.config(state='readonly')

#Etiqueta
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, columnspan=2)

def enviar():
    #Modificamos el texto dfel label
    etiqueta1.config(text=entrada_var1.get())
    entrada_var1.set('')
    #Message box
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje informativo', mensaje1 + 'Informativo')
def salir():
    #Para poder salir de la aplicacion usamos el metodo de ventana
    ventana.quit()
    ventana.destroy()
    print('Salimos de la aplicacion')
    sys.exit()




def crear_menu():
    #Configuramos el menu principal
    menu_principal = Menu(ventana)
    menu_archivo = Menu(menu_principal, tearoff=False)
    #Agregamos una nueva opcion al menu de archivo
    menu_archivo.add_command(label='Nuevo')
    #Agregamos separador
    menu_archivo.add_separator()
    #Opcion de salir
    menu_archivo.add_command(label='Salir', command=salir)

    # SUbmenu de ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=False)
    submenu_ayuda.add_command(label='Acerca de ')
    #Agregamos submenu al menu principal
    menu_principal.add_cascade(menu=menu_archivo, label='Archivo')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Acerca de')

    #Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)


#creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)


crear_menu()
ventana.mainloop()