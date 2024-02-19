""" buscando elemento en las listas """

mascotas = ["Wolf", "Dog", "Cat", "Lion", "Bird", "Dog"]

print(mascotas.index("Cat"))

if "Bird" in mascotas:
    print(mascotas.index("Bird"))
else:
    print("pet not found")

print("count: ", mascotas.count("Dog"))
