""" Operadores logicos """

# and, or, not

gas = True
encendido = True

if gas and encendido:
    print("puedes avanzar")

gas = True
encendido = False
if gas or encendido:
    print("puedes avanzar")

gas = False
encendido = True
edad = 18
if not gas and (encendido or edad > 17):
    print("puedes avanzar")
