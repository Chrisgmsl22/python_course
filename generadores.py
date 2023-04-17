#Generadores
#Funcion especial en python, retorna una secuencia de valores, suspende la ejecución
# Yield, regresa los valores poco a poco den nuestra secuencia de valores (no se usa return)
def generador():
    yield 1
    yield 2
    yield 3


#Consumimos el generador a demanda
gen = generador()
#Por medio de la funcion next consumimos el valor
print(next(gen)) #Cada que llamamos el next, se ejecuta el generador
print(next(gen))
print(next(gen))
#print(next(gen))

#Si tratamos de consumir mas valores del generador, manda un error

#Consumiendo los valores del generador con un ciclo dfor
gen = generador()
for valor in gen:
    print(valor)