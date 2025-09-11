** start of main.py **

"""
Pangram
Given a word or sentence and a string of lowercase letters, determine if the word or sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.
"""

"""Solución con set

def is_pangram(sentence, letter_set):
    # Pasar todo a minúsculas
    sentence = sentence.lower()
    # Crear conjunto solo con letras alfabéticas de sentence
    sentence_letters = set(c for c in sentence if c.isalpha())
    letter_set = set(letter_set)  # Crear conjunto de las letras a buscar

    # Verificar que: 
    # 1) sentence solo tenga letras del set
    # 2) Todas las letras del set estén en sentence
    if sentence_letters == letter_set:
        return True
    else:
        return False
"""

#Solución con bucles

def is_pangram(sentence, letter_set):
    sentence = sentence.lower()
    for letra in letter_set:
        if letra not in sentence:
            return False
    # Extra: verificar que no haya letras fuera del set
    for c in sentence:
        if c.isalpha() and c not in letter_set:
            return False
    return True





** end of main.py **

