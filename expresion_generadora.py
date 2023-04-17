# Ejemplo de expresión generadora (es un generador anónimo)
multiplicacion = (valor*valor for valor in range(1, 4))#Una expresión generadora debe estar dentro de paréntesis
print(multiplicacion)
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

#Tambien se puede pasar una expresión generadora a una funcion (sin paréntesis)
import math
suma = sum(valor*valor for valor in range(5))
print(f'Resultado de la suma: {suma}')

lista = ['Juan', 'Pérez']
generador = (valor for valor in lista) #Recuperamos los valores en la lista
print(next(generador))
print(next(generador))
#Podemos recuperar los elementos a demanda

#Crear un string a partir de un generador, creado a partir de una lista
lista = ['Karla', 'Gomez']
#A los elementos le adjuntamos un valor numérico
contador = 0
#Definimos una funcion que nos permita implementar el contador
def incrementar():
    global contador
    contador += 1
    return contador

#Creamos nuestra expresión generador
#La primera es el yield, luego es el for (entre paréntesis )
generador = (f'{incrementar()}. {nombre}' for nombre in lista)

lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada a partir de la lista: {cadena}')

def mi_generador(n):
    for i in range(n):
        yield i

# Llamamos al generador
gen = mi_generador(5)

# Imprimimos los valores generados
for valor in gen:
    print(valor)
