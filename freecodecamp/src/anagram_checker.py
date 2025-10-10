"""
Anagram Checker
Given two strings, determine if they are anagrams of each other (contain the same characters in any order).

Ignore casing and white space.
"""

def are_anagrams(str1, str2):

    #Eliminamos espacios y convertimos a minusculas
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        print(f"'{str1}' and '{str2}' are not anagrams")
        return False
    else:
        print(f"'{str1}' and '{str2}' have the same length, checking letters...")

#Se comparan las letras ordenadas
        if sorted(str1) == sorted(str2):
            print(f"'{str1}' and '{str2}' are anagrams")
            return True
        else:
            print(f"'{str1}' and '{str2}' are not anagrams")
            return False

# Test cases
are_anagrams("Listen", "Silent")  # True
are_anagrams("Hello", "World")    # False
are_anagrams("School master", "The classroom")  # True
are_anagrams("apple", "banana")  # False