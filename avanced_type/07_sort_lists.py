""" ordenando listas """

numeros = [5, 2, 7, 29, 1, 9]

numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
# devuelve una nueva lista sin afectar la anterior
nuevos = sorted(numeros, reverse=False)
print(nuevos)

# ordena por el primer elemento
usuarios = [[4, "Carlos"], [2, "Felipe"], [5, "Pulga"]]
usuarios.sort()
print(usuarios)
usuarios = [["Pulga", 4], ["Felipe", 2], ["Carlos", 5]]
usuarios.sort()
print(usuarios)


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)
print(usuarios)

# usando lambda functions
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
