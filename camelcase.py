** start of main.py **

"""
camelCase
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed.


Passed:1. to_camel_case("hello world") should return "helloWorld".
Passed:2. to_camel_case("HELLO WORLD") should return "helloWorld".
Passed:3. to_camel_case("secret agent-X") should return "secretAgentX".
Passed:4. to_camel_case("FREE cODE cAMP") should return "freeCodeCamp".
Passed:5. to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk") should return "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk".
"""

def to_camel_case(s):
    # Lista de separadores que queremos convertir a espacios
    separadores = ['-', '_']
    # Nueva cadena donde iremos guardando el string solo con espacios
    cadena_solo_espacios = ""

    # Recorremos cada letra/original
    for letra in s:
        if letra in separadores:
            cadena_solo_espacios += " "
        else:
            cadena_solo_espacios += letra
    
    # Ahora separamos las palabras por espacio
    words = cadena_solo_espacios.split(' ')
    
    # Variable para ir formando el resultado final en camelCase
    camelcase = ""
    for i, word in enumerate(words):
        if word == "":
            continue  # Si hay palabras vacías, se ignoran
        if i == 0:
            # Primera palabra toda en minúsculas
            camelcase += word.lower()
        else:
            # Primera letra mayúscula + resto minúscula
            camelcase += word[0].upper() + word[1:].lower()
    
    return camelcase


** end of main.py **

