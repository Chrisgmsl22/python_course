class MiClase:

    #Agregamos un atributo de clase, solo es un valor único, no cambia con el número de instancias
    variableClase = 'Valor variable clase'

    def __init__(self, variableInstancia):
        self.variableInstancia = variableInstancia

    #Métodos estáticos
    @staticmethod #decorador de acceso estático
    def mostrarEstatico():
        MiClase.variableClase = 'Accedida desde la creación de la clase'
        return MiClase.variableClase

    #Método de clase, no estático
    @classmethod
    def mostrarClaseMetodo(cls): #cls hace referencia a la clase misma
        print(cls.variableClase)

    #Metodo de instancia
    def metodo_instancia(self):
        self.mostrarClaseMetodo()
        self.mostrarEstatico()
        print(self.variableClase)
        print(self.variableInstancia)
        #self.metodo_instancia()

MiClase.variableClase = 'This is nice'
print(MiClase.variableClase)

MiClase.alVuelo = 'Rápido'
print(MiClase.alVuelo)


print(MiClase.mostrarEstatico())
MiClase.mostrarClaseMetodo()


#Creamos un nuevo objeto
miObjeto1 = MiClase('variable Instancia')

miObjeto1.mostrarEstatico()
miObjeto1.metodo_instancia()