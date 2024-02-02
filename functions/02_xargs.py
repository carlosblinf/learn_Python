""" xargs: argumentos con iterables"""


def sum(*numeros):
    result = 0
    for n in numeros:
        result += n
    print("El resultado es: ", result)


sum(2, 2)
sum(2, 2, 5, 6)
