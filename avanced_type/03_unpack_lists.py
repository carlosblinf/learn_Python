""" desempaquetar listas """

numeros = list(range(1,10))
primero, segundo, *otros, ultimo = numeros
print(primero, segundo, otros, ultimo)