""" Flujo while """

n = 1
while True:
    print(n)
    n += 1
    if n > 5:
        print("termine")
        break

numero = 1
while numero < 100:
    print(numero)
    numero *= 2

print("*** Nueva terminal ***")
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print("->", comando if comando.lower() != "salir" else "Bye")
