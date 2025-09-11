** start of main.py **

"""S P A C E J A M
Given a string, remove all spaces from the string, insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces).


Passed:1. space_jam("freeCodeCamp") should return "F  R  E  E  C  O  D  E  C  A  M  P".
Passed:2. space_jam("   free   Code   Camp   ") should return "F  R  E  E  C  O  D  E  C  A  M  P".
Passed:3. space_jam("Hello World?!") should return "H  E  L  L  O  W  O  R  L  D  ?  !".
Passed:4. space_jam("C@t$ & D0g$") should return "C  @  T  $  &  D  0  G  $".
Passed:5. space_jam("allyourbase") should return "A  L  L  Y  O  U  R  B  A  S  E"."""


def space_jam(s):
    spacejam_string = ""

    # Creamos una lista vacía donde guardaremos solo las letras, sin espacios
    letras_sin_espacio = []
    
    # Recorremos cada letra de la cadena original
    for letra in s:
        if letra != ' ':
            letras_sin_espacio.append(letra)  # Añadimos solo si no es un espacio

    # Ahora recorremos esta nueva lista para construir el string final
    for i, letra in enumerate(letras_sin_espacio):
        if i != len(letras_sin_espacio) - 1:
            spacejam_string += letra.upper() + '  '
        else:
            spacejam_string += letra.upper()

    return spacejam_string


** end of main.py **

