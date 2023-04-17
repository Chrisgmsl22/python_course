from NumerosIdenticosException import NumerosIdenticosException

#Arrojamos una excepcion
resultado = None


try:
    a = int(input('Ingresa el primer número: _'))
    b = int(input('Ingresa el segundo número: _'))
    if a == b:
        raise NumerosIdenticosException('Numeros idénticos') #Arrojar el tipo de texto
    resultado = a / b
#Siempre la clase de menor jerarquía primero
except ZeroDivisionError as zDE:
    print(f'Ocurrió un error: {zDE}, [{type(zDE)}]')
except TypeError as tE:
    print(f'Ocurrió un error: {tE}, [{type(tE)}]')
except Exception as e:
    print(f'Ocurrió un error: {e}, [{type(e)}]')
#Por último se coloca la excepción más genérica
else:
    print('No se arrojó ninguna excepción'.center(50, '*'))
finally:
    print('Always On ')

    #la sintaxis para el manejo de errores es try -> except
    #bloque else se ejecuta en caso de que no se lance ninguna excepcion
    #Finally se ejecuta haya excepción o no
print(f'Resultado: {resultado} \n continuamos')