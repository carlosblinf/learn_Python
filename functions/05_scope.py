""" Scope o alcance """

# global scope
saludo = "Hola a todos"


def saludar():
    # inner scope saludar
    print(saludo)  # local variable referenced before assigment
    saludo = "Hola mundo"


def saludarPersona():
    # inner scope saludarPersona
    saludo = "Hola Carlos"
    print(saludo)


saludar()
saludarPersona()
