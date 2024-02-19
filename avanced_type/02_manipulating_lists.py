""" Manipulando listas """

mascotas = ["Wolf", "Dog", "Cat", "Lion", "Bird"]
print(mascotas)
mascotas[0] = "Bear"
print(mascotas)
print(mascotas[2:])
print(mascotas[:3])
print(mascotas[-1])
print(mascotas[::2]) # even
print(mascotas[1::2])

numeros = list(range(21))
print(numeros)
print(numeros[1:15:2])
