""" tuplas """
# la tuplas son tipo de datos inmutables
numeros_tupla = (1, 2, 3) + tuple(range(4, 10))
print(numeros_tupla)

punto = tuple([1, 2])

menos_numeros = numeros_tupla[:3]
print(menos_numeros)

primero, segundo, *otors = numeros_tupla
print(primero, segundo, otors)
