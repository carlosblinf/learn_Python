""" Scope o alcance """

# global scope
saludo = "Hola a todos"


def saludar():
    # inner scope saludar
    saludo = "Hola mundo"
    print(saludo)


def saludarPersona():
    # inner scope saludarPersona
    saludo = "Hola Carlos"
    print(saludo)


saludar()
saludarPersona()
