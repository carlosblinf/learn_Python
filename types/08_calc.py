""" Simple calculadora """

n1 = input("ingrese el 1er numero\n")
n2 = input("ingrese el 2do numero\n")
n1 = int(n1)
n2 = int(n2)
sum = n1 + n2
rest = n1 - n2
mult = n1 * n2
div = n1 / n2

message = f"""
Para los numeros {n1} y {n2},
la suma es: {sum},
la resta es: {rest},
la multiplucacion es: {mult}
la divicion es: {div}
"""
print(message)
