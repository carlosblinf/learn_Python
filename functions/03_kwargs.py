""" kwargs: argumentos con claves o llaves"""


def get_product(**datos):
    print(datos)


def get_user(**datos):
    print(datos["id"], datos["name"], datos["email"])


# imprime un diccionario
get_product(id="id")
get_product(id="id", name="Iphone", desc="Telefono Iphone")

get_user(id=1, name="Carlos", email="carlosblinf@gmail.com")
