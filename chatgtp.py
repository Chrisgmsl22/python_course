import tkinter as tk
from tkinter import ttk, messagebox

def iniciar_sesion():
    # Aquí puedes poner la lógica para iniciar sesión
    username = username_entry.get()
    password = password_entry.get()

    # Aquí puedes poner la lógica para verificar el username y la contraseña
    if username == "usuario" and password == "password":
        # Si los datos son correctos, puedes mostrar un mensaje de éxito
        tk.messagebox.showinfo("Login", "¡Bienvenido {}!".format(username))
    else:
        # Si los datos son incorrectos, puedes mostrar un mensaje de error
        tk.messagebox.showerror("Error", "Usuario o contraseña incorrectos")


def registrarse():
    # Aquí puedes poner la lógica para registrarse
    pass

def borrar_datos():
    # Aquí puedes poner la lógica para borrar los datos de las casillas
    pass

def olvide_mi_password():
    # Aquí puedes poner la lógica para recuperar la contraseña
    pass

# Creamos la ventana principal
root = tk.Tk()
root.title("Login")

# Creamos los widgets
username_label = ttk.Label(root, text="Username:")
username_entry = ttk.Entry(root)

password_label = ttk.Label(root, text="Password:")
password_entry = ttk.Entry(root, show="*")

iniciar_sesion_button = ttk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
registrarse_button = ttk.Button(root, text="Registrarse", command=registrarse)
borrar_datos_button = ttk.Button(root, text="Borrar Datos", command=borrar_datos)
olvide_mi_password_button = ttk.Button(root, text="Olvidé mi contraseña", command=olvide_mi_password)

# Ubicamos los widgets en la ventana
username_label.grid(column=0, row=0, padx=5, pady=5)
username_entry.grid(column=1, row=0, padx=5, pady=5)

password_label.grid(column=0, row=1, padx=5, pady=5)
password_entry.grid(column=1, row=1, padx=5, pady=5)

iniciar_sesion_button.grid(column=0, row=2, padx=5, pady=5)
registrarse_button.grid(column=1, row=2, padx=5, pady=5)
borrar_datos_button.grid(column=0, row=3, padx=5, pady=5)
olvide_mi_password_button.grid(column=1, row=3, padx=5, pady=5)

# Mostramos la ventana
root.mainloop()
