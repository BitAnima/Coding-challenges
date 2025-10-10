** start of main.py **

"""Vowel Repeater
Given a string, return a new version of the string where each vowel is duplicated one more time than the previous vowel you encountered. For instance, the first vowel in the sentence should remain unchanged. The second vowel should appear twice in a row. The third vowel should appear three times in a row, and so on.

The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
The original vowel should keeps its case.
Repeated vowels should be lowercase.
All non-vowel characters should keep their original case.

Tests
Waiting:1. repeat_vowels("hello world") should return "helloo wooorld".
Waiting:2. repeat_vowels("freeCodeCamp") should return "freeeCooodeeeeCaaaaamp".
Waiting:3. repeat_vowels("AEIOU") should return "AEeIiiOoooUuuuu".
Waiting:4. repeat_vowels("I like eating ice cream in Iceland") should return "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"."""

def repeat_vowels(text):
    vocales = "aeiouAEIOU"
    resultado = ""
    contador_vocal = 0
    for letra in text:
        if letra in vocales:
            contador_vocal += 1
            # La primera aparición conserva el caso original,
            # el resto son minúsculas
            resultado += letra + letra.lower() * (contador_vocal - 1)
        else:
            resultado += letra
    return resultado




** end of main.py **

