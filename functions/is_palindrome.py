""" Palindromos, se escriben igual al derecho y al reves """

# abba, reconocer, ana


def trim(text):
    trim_string = ""
    for char in text:
        if char != " ":
            trim_string += char
    return trim_string


def reverse(text):
    reverse_string = ""
    largo = len(text)
    for index in range(largo):
        char = text[largo-1-index]
        reverse_string += char
    return reverse_string


def es_palindromo(text=""):
    trim_text = trim(text)
    reverse_trim = reverse(trim_text)
    return reverse_trim.lower() == trim_text.lower()


# print("Hola Mundo", reverse(trim("Hola Mundo")))
print("abba", es_palindromo("abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
