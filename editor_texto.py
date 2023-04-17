import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
class Editor(tk.Tk):
    def __init__(self):
        super(Editor, self).__init__()
        self.title('CursoPython - Editor de Texto')
        #Configuracion tamaño mínimo de la ventana
        self.rowconfigure(0, minsize=600, weight=1)
        #Primer columna se acopla al ancho de los elementos
        self.columnconfigure(1, minsize=600, weight=1)
        #Campo de texto (solo definimos variable)
        self.campo_texto = tk.Text(self, wrap=tk.WORD)
        #Atributo de archivo
        self.archivo = None
        #Atributo isFileLoaded?
        self.is_file_loaded = False
        #Creacion de componentes de nuestra aplicacion
        self._crear_componentes()
        #Crear menu
        self._crear_menu()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir', command=self._abrir_archivo) #TODO
        boton_guardar = tk.Button(frame_botones, text='Guardar', command=self._guardar)
        boton_guardar_como = tk.Button(frame_botones, text='Guardar como...', command=self._guardar_como)
        #Los vamos a expendir de manera horizontal (sticky='WE')
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', pady=5, padx=5)
        boton_guardar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        #Se coloca el frame de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')
        #Agregamos el campo de texto, se expandirá por completo el espacio disponible que le reste
        self.campo_texto.grid(row=0, column=1, sticky='nswe')

    def _crear_menu(self):
        #Creamos el menu de la app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        #Agregamos las opciones a nuestro menu
        #Agregamos menu archivo
        menu_archivo = tk.Menu(menu_app, tearoff=False)
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)
        #Agregamos las opciones de menu_archivo
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar)
        menu_archivo.add_command(label='Guardar como...', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)
    def _abrir_archivo(self):
        #Abrimos el archivo para edicion(R/W)
        self.is_file_loaded = askopenfile(mode='r+')
        #Eliminamos el texto anterior
        self.campo_texto.delete(1.0, tk.END)
        #Revisamos si hay un archivo
        if not self.is_file_loaded:
            return
        #Abrimos el archivo en modo lectura/escritura, como un recurso
        with open(self.is_file_loaded.name, 'r+') as self.archivo:
            #leemos el contenido
            texto = self.archivo.read()
            #Insertamos el contenido del archivo en el campo de texto
            self.campo_texto.insert(1.0, texto)
            #Modificamos el titulo de la aplicacion
            self.title(f'*Editor texto - {self.archivo.name}')

    def _guardar(self):
        #Si ya se abrió previamente el archivo, lo sobreescribimos
        if self.is_file_loaded:
            #Salvamos el archivo(lo abrimos en modo escritura)
            with open(self.archivo.name, 'w') as self.archivo:
                #Leemos el contenido de la caja de texto
                texto = self.campo_texto.get(1.0, tk.END)
                #Escribimos el contenido al mismo archivo
                self.archivo.write(texto)
                #Cambiamos el nombre del titulo de la app
                self.title(f'Editor texto - {self.archivo.name}')
        else:
            self._guardar_como()

    def _guardar_como(self):
        #Salvamos el archivo actual como un nuevo archivo
        self.archivo = asksaveasfilename(
            defaultextension='py',
            filetypes=[('Archivos Python', '*.py'), ('Todos los archivos', '*.*')]
        )
        if not self.archivo:
            return
        #Abrimos el archivo en modo escritura
        with open(self.archivo, 'w') as archivo:
            #Leemos el contenido de la caja de texto
            texto = self.campo_texto.get(1.0, tk.END)
            #Escribimos el contenido al nuevo archivo
            archivo.write(texto)
            #Cambiamos el nombre del archivo
            self.title(f'Editor texto - {archivo.name}')
            #indicamos que ya se ha abierto un archivo
            self.is_file_loaded = archivo


if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()