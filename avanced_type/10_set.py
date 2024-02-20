""" Sets: conjuntos o grupos """

primer = {1, 1, 2, 1, 4, 5, 3, 5}
print(primer)

primer.add(4)
print(primer)
primer.remove(1)
print(primer)

lista = [3, 2, 5, 6, 7]
print("lista", lista)
segundo = set(lista)
print("set", segundo)

# operadores de los set
print(primer | segundo)
print(primer & segundo)
print(primer - segundo)
print(primer ^ segundo)  # diferencia simetrica

if 5 in primer:
    print("si esta")
