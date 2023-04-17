#Definimos una variable global
contador = 0

def mostrar_contador():
    print(f'Valor del contador: {contador}')

def modificar_contador(nuevoValor):
    global contador
    contador = nuevoValor

modificar_contador(5)
mostrar_contador()