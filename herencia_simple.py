#Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos) #El elemento ya debe de ser una lista en sí misma

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento) #Elementos es un atributo protegido

    #Sobreescribimos un método built in
    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort() #Ordenamos los elementos de la lista

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos})'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos=[]): #Le asignamos una lisa vacía por defecto
        super().__init__(elementos) #inicializamos los elementos
        #Ordenamos los elementos una vez inicializados
        self.ordenar()
    def agregar_elemento(self, elemento):
        super().agregar_elemento(elemento)
        #Tambien ordenamos el nuevo elemento
        self.ordenar()

#Essta lista solo acepta numeros
class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento) #TO-DO
        #Inicializamos la lista
        super().__init__(elementos)

    def _validar(self, elemento):
        #Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero: {elemento}')

    #Sobreescribimos el metodo de agregar, de la clase padre
    def agregar_elemento(self, elemento):
        #Primero validamos
        self._validar(elemento)
        #Despues lo agregamos a la lista
        super().agregar_elemento(elemento)
        super().ordenar()


lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)

lista_ordenada = ListaOrdenada([4, 3,6 , 8, 19, -1])
print(lista_ordenada)
lista_ordenada.agregar_elemento(100)
print(lista_ordenada)
print(len(lista_ordenada))

lista_enteros = ListaEnteros([1, 2, 6, 4, 5,])
print(lista_enteros)