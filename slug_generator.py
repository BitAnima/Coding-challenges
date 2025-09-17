"""
Slug Generator
Given a string, return a URL-friendly version of the string using the following constraints:

All letters should be lowercase.
All characters that are not letters, numbers, or spaces should be removed.
All spaces should be replaced with the URL-encoded space code %20.
Consecutive spaces should be replaced with a single %20.
The returned string should not have leading or trailing %20."""

import re

def generate_slug(str):

    str = str.lower()
    str = re.sub(r"[^a-z0-9 ]", "", str) #el ^ dentro de los corchetes actúa como negación. Elimina todo lo que no sea letra minúscula, número o espacio
    str = re.sub(r" +", " ", str) #r" +": expresión regular que significa “uno o más espacios” (+ quiere decir “uno o más” de lo que está antes, aquí un espacio).
    str = str.strip() #Elimina espacios al principio y al final
    str = re.sub(r" ", "%20", str)      

    print(f"{str}")

    return str

"""Para minúsculas: str.lower()
Para filtrar letras y números (opcionalmente espacios): usando un ciclo for, comprensión de listas, o re.sub()
Para unir palabras con %20: puedes usar .split() y luego .join()
Para eliminar espacios (al inicio o final): .strip()
Para compactar varios espacios en uno solo: también puedes usar re.sub(r" +", " ", texto)"""

generate_slug("helloWorld") # "helloworld".
generate_slug("hello world!") # "hello%20world".
generate_slug(" hello-world ") # "helloworld".
generate_slug("hello  world") # "hello%20world".
generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") # "h3110%20w0r1d".