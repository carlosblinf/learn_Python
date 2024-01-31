""" Strings """

nombre_curso = "Ultimate Python"  # '' or ""
descripcion_curso = """
Ultimate Python,
es un buen curso con el que estoy aprendiendo python,
conociendo los detalles para desarrollar aplicaciones de IA y LLM.
"""
print(nombre_curso, descripcion_curso)

print(len(nombre_curso))
print(len(descripcion_curso))
print(nombre_curso[0])  # string are array of bytes or characters
print(nombre_curso[0:8])  # substrings [index:characters]
print(nombre_curso[9:])  # print Python
print(nombre_curso[:8])  # print Ultimate
print(nombre_curso[:])  # print Ultimate Python
