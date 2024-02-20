""" diccionarios: sirven para representar objetos o json """

# las key son str
punto = {"x": 2, "y": 5}
print(punto)
print(punto["x"])
print(punto.get("y"))
print(punto.get("z"))  # None
punto["z"] = 3
print(punto)
print(punto.get("lala", 0))

del punto["x"]
print(punto)

for key in punto:
    print(punto[key])

for valor in punto.items():
    print(valor)

for key, value in punto.items():
    print(key, value)

usuarios = [
    {"id": 1, "name": "Carlos"},
    {"id": 2, "name": "Pepe"},
    {"id": 3, "name": "Juan"}
]
print(usuarios)

for u in usuarios:
    print(u["name"])
