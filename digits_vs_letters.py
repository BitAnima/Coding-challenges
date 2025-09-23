"""Digits vs Letters
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.

Digits consist of 0-9.
Letters consist of a-z in upper or lower case.
Ignore any other characters."""


def digits_or_letters(s):

    is_digit = 0
    is_letter = 0

    for character in s:
        if character.isdigit():
            is_digit += 1
        elif character.isalpha():
            is_letter += 1
    if is_digit > is_letter:
        print("There are more digits than letters.")
        return "digits"
    elif is_letter > is_digit:
        print("There are more letters than digits.")
    else:
        print("There are same amount of digits.")
        return "tie"

    return "letters"

digits_or_letters("abc123")# "tie".

digits_or_letters("a1b2c3d")# "letters".

digits_or_letters("1a2b3c4")# "digits".

digits_or_letters("abc123!@#DEF")# "letters".

digits_or_letters("H3110 W0R1D")# "digits".

digits_or_letters("P455W0RD")# "tie".