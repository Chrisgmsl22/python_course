#Las funciones en python son ciudadanas de primera clase
#First class citizens

#Definimos la función
def sumar(a, b):
    return a + b
#1. Asignar una función a una variable (no se usan paréntesis)
mi_funcion = sumar

#Verificamos el tipo de la variable
print(type(mi_funcion))

#Llamamos la función a través de la variable
resultado = mi_funcion(5, 5)

print(resultado)

#2, Función como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a,b)}')

operacion(4,5 ,sumar)


#3. podemos retornar función
def retornar_funcion():
    #Retornamos una funcion
    return sumar

mi_funcion_retorna = retornar_funcion()
print(mi_funcion_retorna)