#Decoradores de clase
#Meta programacion, permite transformar de manera programatica nuestra clase
#Similar a los decoradores de funciones
import inspect


def decorador_repl(cls):
    print('Se ejecuta el decorador de nuestra clase')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')
    #Revisamos los atributos de la clase con el método vars
    atributos = vars(cls)
    #Iteramos cada uno de los atributos
    for nombre, atributo in atributos.items():
        print(nombre, atributo)

    #Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método init')

    #Firma del método init
    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del método init: {firma_init}')
    #Recuperamos los parámetros exepto el primero
    parametros_init = list(firma_init.parameters)[1:]

    #revisamos si por cada parametro, se tienen getters
    for parametro in parametros_init:
        #property es de tipo built in, para preguntar si se está utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro: {parametro}')

    #Creamos el método repl, dinámicamente
    def metodo_repr(self):
        #Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre de la clase: {nombre_clase}')
        #Obtenemos los nombres de las propiedades y sus valores dinamicamente
        #EXpresión generadora para crear nombre_atr=valor_art
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        #Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        #Creamos la forma del método __repr__ sin su nombre
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'

        return resultado_metodo_repr
    #Agregar dinámicamente el método repl a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    #Regresamos el objeto de la clase
    return cls

@decorador_repl
class Persona:
    def __init__(self, nombre, apellido):
        print('Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido

    def __repr__(self):
        return f'Persona({self._nombre}, {self._apellido})'

persona1 = Persona('Juan', 'Perez')
print(persona1)

#Para usar el decorador en otra clase, se tienen que agregarle los getters a los atributos de la clase
#Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr)