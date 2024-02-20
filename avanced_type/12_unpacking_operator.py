""" operador desempaquetar """

lista1 = [1, 2, 3, 4]
# print(1, 2, 3, 4)
print(*lista1)
tupla = tuple(lista1)
print(*tupla)

lista2 = [5, 6]
combinada = [*lista1, *lista2]
print(combinada)


punto1 = {"x": 1}
punto2 = {"y": 2}
nuevo_punto = {**punto1, **punto2}
print(nuevo_punto)
punto1 = {"x": 1, "y": "hola"}
nuevo_punto = {**punto1, **punto2}  # asigna de derecha a izquierda
print(nuevo_punto)
punto2 = {"x": 10, "lala": "hola", "y": 2, "z": "mundo"}
nuevo_punto = {**punto1, **punto2}
print(nuevo_punto)
