"""Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
Input = "The sunset sets at twelve o' clock."
Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
StringsFundamentals
"""

def alphabet_position(text):
    """
    Convierte cada letra del texto a su posición en el alfabeto (a=1, b=2, ..., z=26).
    Ignora cualquier carácter que no sea una letra.
    Devuelve las posiciones como una cadena de números separados por espacios.

    Parámetros:
        text (str): La cadena de entrada.

    Retorna:
        str: Cadena con las posiciones de las letras, separadas por espacios.

    Ejemplos:
        alphabet_position("abc")      # "1 2 3"
        alphabet_position("Hello!")   # "8 5 12 12 15"
        alphabet_position("")         # ""
    """
    
    # Generar lista de valores vacía
    values_list = []
    
    # Convertir el string a minúsculas
    lower_case_text = text.lower()
    
    # Filtrar caracteres que sean letras
    """for letter in lower_case_text:
        if letter.isalpha():
            # Para cada letra, obtener su posición usando ord
            value = ord(letter) - ord('a') + 1
            # Guardar la posición en una lista
            values_list.append(str(value))"""
            
    # Usando list comprehension para filtrar y transformar en una sola línea
    values_list = [str(ord(letter) - ord('a') + 1) for letter in lower_case_text if letter.isalpha()]

    
    # Unir la lista en un string separado por espacios
    return ' '.join(values_list)