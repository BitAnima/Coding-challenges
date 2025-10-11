"""Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!"""

# Importamos el módulo de expresiones regulares

import re

def create_phone_number(n):
    # Guardamos la lista como un string
    n = ''.join(str(num) for num in n)
    # Almacenamos el patrón en la variable pattern
    pattern = r"(\d{3})(\d{3})(\d{4})"
    # Asignamos un formato a cada grupo capturado
    formatted_number = re.sub(pattern, r'(\1) \2-\3', n)
    # Devolvemos el número formateado
    return formatted_number