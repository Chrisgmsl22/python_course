#Profundizando en el uso de sets
#Un set es una colección de elementos unicos y es mutable
#Los elementos de un set deben ser inmutables
conjunto = {'Juan', True, 18.90}
print(conjunto)

#Para definir un set vacío
conjunto = {}
print(type(conjunto))
conjunto = set()
print(type(conjunto))
print(conjunto)

conjunto.add('Carlos')
print(conjunto)
#Un set tiene valores únicos
conjunto = set([4, 5, 7, 8, 4])
print(conjunto)

#Podemos agregar más elementos o incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20, 30, 40])
print(conjunto)

#Copiar un set (solamente se copiarán las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

#Verificar igualdad
print(f'Es igual al contenido? : {conjunto == conjunto_copia}')
print(f'Es la misma referencia?: {conjunto is conjunto_copia}')

#Operaciones de conjuntos utilizando sets
#Personas con distintad caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'María'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'María'}

#Recuperamos todos los elementos con ojos color cafe y pelo rubio (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))
#Invertimos el orden con el mismo resultado
print(pelo_rubio.union(ojos_cafe))

#(Intersection) recuperamos solo las personas con ojos cafe y pelo rubio (conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

#Difference, personas de pelo nnegro, pero sin ojos cafe
#Personas que se encuentran en el primer set, pero no en el segundo
print(pelo_negro.difference(ojos_cafe))


#Diferencia asimetrica, regresa rodos los elementos, menos las coincidencias de ambos elementos
#Pelo negro u ojos cafe, pero NO ambos
print(pelo_negro.symmetric_difference(ojos_cafe))

#Preguntar si un set está contenido en el otro (subset, subconjunto)
print(menores_30.issubset(pelo_negro))

#Preguntar si un set tiene a otro set
#Revisar si los elementos del primer set estan contenidos en el segundo seyt
print(menores_30.issuperset(pelo_negro))

#Preguntar si los de pelo negro no tienen pelo rubio
print(pelo_negro.isdisjoint(pelo_rubio))