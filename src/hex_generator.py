"""
Hex Generator
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function # "Invalid color".
The function # a random six-character hex color code where the input color value is greater than any of the others.
Example of valid outputs for a given input:
Input	Output
"red"	"FF0000"
"green"	"00FF00"
"blue"	"0000FF"
"""

import random

def rgb_to_hex (r, g, b):
    #print(f"{r:02X}{g:02X}{b:02X}")
    return f"{r:02X}{g:02X}{b:02X}" # :02X -> indica que se deben usar dos dígitos y rellenar con ceros si es necesario. X convierte el número a hexadecimal en mayúsculas

def generate_hex(color):

    colors = ["blue", "green", "red"]

    if color not in colors:
        return(f"Invalid color")
    else:
        main_color = color

    print(f"Main color: {main_color}")

    """Los colores RGB tienen asignados números de 0 a 255.
    El color dominante debe estar comprendido entre 170 y 255 y los secundarios entre 0 y 150"""

    main_color = random.randint(170, 255)
    secondary1 = random.randint (0, 150)
    secondary2 = random.randint (0, 150)

    if color == "red":
        result = rgb_to_hex(main_color, secondary1, secondary2)
    elif color == "green":
        result = rgb_to_hex(secondary1, main_color, secondary2)
    elif color == "blue":
        result = rgb_to_hex(secondary1, secondary2, main_color)  


    return result

result = generate_hex("yellow") # "Invalid color".
print(f"{result}")
result = generate_hex("red") # a six-character string.
print(f"{result}")
result = generate_hex("red") # a valid six-character hex color code.
print(f"{result}")
result = generate_hex("red") # a valid hex color with a higher red value than other colors.
result = print(f"{result}")
# two different hex color values where red is dominant.
result1 = generate_hex("red")
result2 = generate_hex("red")
print(f"{result1}")
print(f"{result2}")
# two different hex color values where green is dominant.
result1 = generate_hex("green")
result2 = generate_hex("green")
print(f"{result1}")
print(f"{result2}")
# two different hex color values where blue is dominant.
result1 = generate_hex("blue")
result2 = generate_hex("blue")
print(f"{result1}")
print(f"{result2}")
