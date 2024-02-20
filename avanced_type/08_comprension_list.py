""" listas de comprension """

usuarios = [
    ["Pulga", 4],
    ["Felipe", 2],
    ["Carlos", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# nombres = [expression for item in items]
nombres = [usuario[0] for usuario in usuarios]  # transformando lista
print(nombres)
nombres_filtrados = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres_filtrados)

nombres1 = list(map(lambda usuario: usuario[0], usuarios))
print(nombres1)
menos_usuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menos_usuarios)
