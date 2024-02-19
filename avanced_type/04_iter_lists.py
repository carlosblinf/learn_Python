""" iterar listas """

# iterables son las listas, los str y el resultado de la funcion range
mascotas = ["Wolf", "Dog", "Cat", "Lion", "Bird"]

for mascota in mascotas:
    print(mascota)

for tupla in enumerate(mascotas):  # enumerate devuelve iterables
    print(tupla)

for index, mascota in enumerate(mascotas):  # enumerate devuelve iterables
    print(index, mascota)
