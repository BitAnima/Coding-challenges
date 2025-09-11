** start of main.py **

"""
RGB to Hex
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	"#010203"
Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
"""

def rgb_to_hex(rgb):
    # Quitar las palabras 'rgb', los paréntesis y dejar solo los números separados por coma
    numbers = rgb.replace('rgb', '').replace('(', '').replace(')', '').split(',')

    # Convertir cada string de la lista a int, para obtener los valores numéricos de rojo, verde y azul
    r, g, b = [int(n) for n in numbers]

    # Crear el string hexadecimal:
    # - El símbolo '#' indica que es un color hex
    # - {:02x} convierte el número a hexadecimal de 2 dígitos (rellena con 0 a la izquierda si hace falta)
    # - Se hace para r, g y b, y se concatenan juntos
    return f"#{r:02x}{g:02x}{b:02x}"


** end of main.py **

