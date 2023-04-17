#Ejemplo atributos publicos, protegidos y privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado #solo se pueden usar dentro de la clase


objeto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')

#Acceso al atributo publico
print(objeto.publico)
#Modificar valor publico
objeto.publico = 'Nuevo publico'
print(objeto.publico)

#Acceso al valor protegido
#Solo dentro de la misma clase
print(objeto._protegido)
#Modificar igualmente, sin embargo no se consideran buenas prácticas

#Para acceder al valor privado
#print(objeto.__privado)
#pero convierte ...
