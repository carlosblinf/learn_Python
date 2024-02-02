""" Calculadora un poco mas avanzada """

print(" *** Calculadora *** ")
print("""Las operaciones son:
 suma(+), resta(-), multi(*), div(/) o salir para abandonar.
""")

result = ""
while True:
    if not result:
        result = input("Ingrese un numero entero: ")
        if result.lower() == "salir":
            print("-> Programa terminado")
            break
    result = int(result)

    command = input("Entre una operacion: ")
    if command.lower() == "salir":
        print("-> Programa terminado")
        break

    numero = input("Ingrese otro numero entero: ")
    if numero.lower() == "salir":
        print("-> Programa terminado")
        break
    numero = int(numero)

    if command.lower() == "suma" or command == "+":
        result += numero
    elif command.lower() == "resta" or command == "-":
        result -= numero
    elif command.lower() == "multi" or command == "*":
        result *= numero
    elif command.lower() == "div" or command == "/":
        if numero != 0:
            result /= numero
        else:
            print("-> No puede divir por 0")
    else:
        print("-> Operacion incorrecta!")

    print("El resultado es: ", result)
