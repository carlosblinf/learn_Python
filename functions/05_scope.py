""" Scope o alcance """

# global scope
saludo = "Hola a todos"


def saludar():
    # inner scope saludar
    global saludo
    print(saludo)
    saludo = "Hola mundo"


def saludarPersona():
    # inner scope saludarPersona
    saludo = "Hola Carlos"
    print(saludo)

saludar()
print(saludo)
saludarPersona()
