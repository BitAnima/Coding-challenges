** start of main.py **

"""Acronym Builder
Given a string containing one or more words, return an acronym of the words using the following constraints:

The acronym should consist of the first letter of each word capitalized, unless otherwise noted.
The acronym should ignore the first letter of these words unless they are the first word of the given string: a, for, an, and, by, and of.
The acronym letters should be returned in order they are given.
The acronym should not contain any spaces.


Passed:1. build_acronym("Search Engine Optimization") should return "SEO".
Passed:2. build_acronym("Frequently Asked Questions") should return "FAQ".
Passed:3. build_acronym("National Aeronautics and Space Administration") should return "NASA".
Passed:4. build_acronym("Federal Bureau of Investigation") should return "FBI".
Failed:5. build_acronym("For your information") should return "FYI".
Failed:6. build_acronym("By the way") should return "BTW".
Failed:7. build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily") should return "AUHWPOTIMSH"."""


def build_acronym(s):
    # Lista de palabras que hay que ignorar (excepto si son la primera)
    ignored_words = ["a", "for", "an", "and", "by", "of"]

    # Variable donde se va formando el acrónimo
    acronym = ""

    # Primero, separamos la frase en palabras, usando los espacios como separador
    set_words = s.split(' ')

    # Usamos enumerate para recorrer la lista con el índice (i) y la palabra (word)
    for i, word in enumerate(set_words):
        # Si es la primera palabra (índice 0), siempre la añadimos.
        # Si no es la primera, solo añadimos si no está en la lista de palabras a ignorar
        if i == 0 or word.lower() not in ignored_words:
            if word != "":  # Asegura que no esté vacía (puede haber dobles espacios)
                acronym += word[0].upper()  # Añade la letra inicial en mayúsculas

    # Al terminar el bucle, devolvemos el resultado final
    return acronym

"""
¿Qué hace enumerate?
La función enumerate() en Python permite recorrer una lista y obtener tanto el índice como el valor de cada elemento, al mismo tiempo.

Ejemplo simple:

python
for i, valor in enumerate(['a', 'b', 'c']):
    print(i, valor)
Salida:

text
0 a
1 b
2 c
Donde:

i es el número de la posición (empezando desde 0).

valor es el elemento en esa posición.

¿Por qué lo usamos en tu código?

python
for i, word in enumerate(set_words):
    if i == 0 or word.lower() not in ignored_words:
        acronym += word[0].upper()
i es el número de palabra dentro de la frase (0 es la PRIMERA).

Así, podemos comprobar si es la PRIMERA palabra (i == 0).

word es la palabra que estamos procesando.

Ventaja:
Puedes tomar decisiones distintas para la primera palabra (o para cualquier posición) directamente dentro del bucle, sin variables extra.

Resumen visual del uso:

python
frase = "Por si acaso"
for i, palabra in enumerate(frase.split()):
    print(f"Palabra #{i}: {palabra}")
Salida:

text
Palabra #0: Por
Palabra #1: si
Palabra #2: acaso
"""



** end of main.py **

