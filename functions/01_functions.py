""" Funciones """


def hola():
    print("Hello World")
    print("Ultimate Python")


def saludar(name):
    print(f"Hola {name}")


def welcome(name, last_name="Feliz"):
    print(f"Bienvenido {name} {last_name}")


# definicion de la funcion antes de uso
hola()
saludar("Carlos")
welcome("Carlos", "Brooks")
welcome("Carlos")
# argumentos nombrados
welcome(last_name="Perez", name="Javier")
