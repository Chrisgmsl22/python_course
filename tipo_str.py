from mi_clase import MiClase
#Profundizando en el tipo str

#Concatenación automática en python
mensaje = 'Hola' + ' ' + 'Mundo'
mensaje += ' Universidad' ' ' 'Python'
print(mensaje)

print('Ayuda en python'.center(50, '*'))
help(str)

'''
    Así se crea un comentario de varias líneas
'''

help(MiClase)
print(MiClase.__doc__)


print('Inmutabilidad'.center(50, '+'))
#Profundizando el tipo str
#help(str.capitalize)
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1: {mensaje1}, id: {id(mensaje1)}')
print(f'mensaje2: {mensaje2}, id: {id(mensaje2)} ')


print('Usando JOIN'.center(50, '+'))

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring Boot']
mensaje = ', '.join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'HolaMundo' #Este es un iterable ya que es un arreglo de caracteres
mensaje = '.'.join(cadena)
print(mensaje)

diccionario = {'name': 'John', 'lastname':'Maker', 'age':'33'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')

#Método split
print('Split'.center(50, '+'))
#help(str.split)

cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'Lista cursos: {lista_cursos}')

cursor_separados_coma = 'Java,Python,JS,Angular,React,Spring,Excel'
lista_cursos = cursor_separados_coma.split(',')
print(f'lista cursos: {lista_cursos}')

lista_cursos = cursor_separados_coma.split(',', 12)
print(f'lista cursos: {lista_cursos}')



#Formato a un string
nombre = 'Kevin'
edad = 33
mensaje_con_formato = 'Mi nombre es %s, tengo %s años'%(nombre, edad)

print(f'Mensaje con formato: {mensaje_con_formato}')

persona = ('Karla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es: %.2f'%(persona)
print(mensaje_con_formato)

#Los valores se pueden pasar cuando se está definiendo el formato y cuando se pasan los valores
mensaje_con_formato = 'Hola %s %s. Tu sueldo es: %.2f'
print(mensaje_con_formato%persona)

print('Método format'.center(50, '+'))
nombre = 'Carlos'
edad = 33
sueldo = 3000.00
mensaje_con_formato = 'Nombre {}, Edad {}, Sueldo: {:.2f}'.format(nombre, edad, sueldo)

print(f'Método format: {mensaje_con_formato}')

mensaje_nuevo = 'Nombre {0}, Edad: {1}, Sueldo: {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje_nuevo)

print('Profundizando el método format'.center(50, '+'))

mensaje_nuevo = 'Nombre: {n}, Edad: {e}, Sueldo: {s:.2f}'.format(n = nombre, e = edad, s = sueldo)
print(mensaje_nuevo)

diccionario = {'nombre':'Ivan', 'Edad':'35', 'Sueldo':'8000.00'}
mensaje = 'Nombre {persona[nombre]}, Edad: {persona[Edad]}, Sueldo:{persona[Sueldo]}'.format(persona = diccionario)
print(mensaje)


print('Uso de template literal'.center(50, '+'))

nombre = 'Sergio'
edad = 22
sueldo = 10000
mensaje = f'Nombre: {nombre}, Edad: {edad}, Sueldo: {sueldo},'
print(mensaje)

#El método print tiene ciertas variabtes
print(nombre, edad, sueldo, sep='-')

print('Multiplicación de cadenas'.center(50, '+'))
resultado = 5*'Strike'
print(f'Resultado: {resultado}')

#Multiplicación de tuplas
resultado = 5*('Uva', 'Pera', 'Manzana')
print(f'Resultado: {resultado}')

#Multiplicación de listas
resultado = 10*[0]
print(f'Resultado: {resultado}, largo {len(resultado)}')

#Caracteres de escape
resultado = 'Hola \' Mundo'
print(resultado)


resultado = 'Se va a eliminar el punto .\b'
print(resultado)

#Caracter \
resultado = 'c:\\\\directorio\\Juan'
print(resultado)

#row string
resultado = r'c:\nuevo\juan'
print(resultado)

print('Caracteres UNICODE'.center(50, '+'))

print('Hola\u0020Mundo')
print('Notación simple: ', '\u0041')
print('Notación hexadecimal: \x41')
print('Corazon: \u2665')
print('Cara sonriendo: \U0001f600')
print('Serpiente: \U0001F40D')

print('ASCII'.center(50, '+'))
caracter = chr(64)
print(caracter)

print('Caracteres en Bytes'.center(50, '+'))

#Caracteres en bytes
char_bytes = b'Hola Mundo'
print(char_bytes)

mensaje = b'Universidad Pyhton'
print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

print('Conversión de String a Bytes'.center(50, '+'))
#Conversión str a butes
string = 'Programación con python'
bytes = string.encode('UTF-8') #Juego de caracteres en que se codificará
print(f'Bytes codificados: {bytes}')

#De bytes a string
string2 = bytes.decode('UTF-8')
print(f'String decodificado: {string2}')
print(string2 == string)
