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
    for char in text:
        reverse_string = char + reverse_string
    return reverse_string


def es_palindromo(text=""):
    trim_text = trim(text)
    reverse_trim = reverse(trim_text)
    print(reverse_trim)
    return reverse_trim.lower() == trim_text.lower()


# print("Hola Mundo", reverse(trim("Hola Mundo")))
print("abba", es_palindromo("abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
