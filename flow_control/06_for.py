""" Flujo for """

for numero in range(5):
    print(numero, numero * "hola")

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado")
        break

buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado")
        break
else:
    print(f"numero {buscar} no encontrado\n")


for char in "python":
    print(char)
