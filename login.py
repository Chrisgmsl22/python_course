import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        #Creamos nuestra ventana principal
        self.geometry('300x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        self.resizable(0, 0) #Ya no podemos hacer más grande la ventana
        #Configuración del grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self._crear_componentes()

    def _crear_componentes(self):
        #Elementos de usuario
        user_label = ttk.Label(self, text='Username')
        user_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)

        self.user_entry = ttk.Entry(self)
        self.user_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        #Password
        pass_label = ttk.Label(self, text='Password: ')
        pass_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)

        self.pass_entry = ttk.Entry(self, show='*')
        self.pass_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        #Boton login
        login_button = ttk.Button(self, text='Login', command=self._login)
        login_button.grid(row=3, columnspan=2)

    #Boton y sus funcionalidades
    def _login(self):
        messagebox.showinfo('Loggin data',
                            f'usuario: {self.user_entry.get()},'
                            f'Password: {self.pass_entry.get()}')













#Ejecutamos la ventana
if __name__ == '__main__':
    login_ventana = LoginWindow()
    login_ventana.mainloop()