""" agregando y eliminando de una lista """

mascotas = ["Wolf", "Dog", "Cat", "Lion", "Bird", "Dog"]

mascotas.insert(1, "Pig")
print(mascotas)
mascotas.append("Horse")
print(mascotas)
mascotas.remove("Dog")  # delete first match
print(mascotas)
mascotas.pop()
print(mascotas)
mascotas.pop(1)
print(mascotas)
del mascotas[0]
print(mascotas)
mascotas.clear()
print(mascotas)
