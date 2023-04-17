#Unpacking

valores = 1, 2 ,3 #Estamos creando una tupla de valores

print(valores)
print(type(valores))

valor1, valor2, *valor3 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#Del lado derechod definimos la tupla, del izquiero el orden en el que se manda la información

print(valor1, valor2, valor3)

def regresar_varios_datos():
    return 1, 3, 4

valor1, *valor2 = regresar_varios_datos()
print(valor1, valor2)

help(str.partition)

variable = '17:30:99'.partition(':')
print(type(variable))
print(variable)