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
