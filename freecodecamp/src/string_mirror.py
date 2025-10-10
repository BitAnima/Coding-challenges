"""String Mirror
Given two strings, determine if the second string is a mirror of the first.

A string is considered a mirror if it contains the same letters in reverse order.
Treat uppercase and lowercase letters as distinct.
Ignore all non-alphabetical characters."""


def clean_strings(str1, str2):
    #Para procesar todos los caracteres y no sólo el primero, se debe utilizar compresión de listas
    clean_string1 = "".join(character for character in str1 if character.isalpha())
    print(clean_string1)

    clean_string2 = "".join(character for character in str2 if character.isalpha())
    print(clean_string2)

    return clean_string1, clean_string2

def is_mirror(str1, str2):

    clean_string1, clean_string2 = clean_strings(str1, str2)

    """El método reverse() no funciona con cadenas en Python porque son inmutables. Para invertir cadenas se debe utilizar slicing
    
    reversed_string = clean_string1[::-1]
    
    Sintaxis [inicio:fin:paso] -> Los dos puntos con el -1 significan: Sin inicio ni fin (se toma toda la cadena).
    Paso -1: recorre la cadena de atrás hacia adelante (la invierte)."""

    #También se puede utilizar compresión de listas y la función reversed combinada con ''.join().
    reversed_string = "".join(reversed(clean_string1))

    print(reversed_string)
    if reversed_string == clean_string2:
        return True

    else:
        return False


def test_helloworld_false():
    assert is_mirror("helloworld", "helloworld") is False
def test_helloworld_true():
    assert is_mirror("Hello World", "dlroW olleH") is True
def test_racecar_true():
    assert is_mirror("RaceCar", "raCecaR") is True
def test_racecar_false():
    assert is_mirror("RaceCar", "RaceCar") is False
def test_mirror_false():
    assert is_mirror("Mirror", "rorrim") is False
def test_hello_world_upper():
    assert is_mirror("Hello World", "dlroW-olleH") is True
def test_hello_world_exclamation():
    assert is_mirror("Hello World", "!dlroW !olleH") is True
