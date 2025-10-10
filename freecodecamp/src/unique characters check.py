** start of main.py **

"""
Unique Characters
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.

Waiting:1. all_unique("abc") should return True.
Waiting:2. all_unique("aA") should return True.
Waiting:3. all_unique("QwErTy123!@") should return True.
Waiting:4. all_unique("~!@#$%^&*()_+") should return True.
Waiting:5. all_unique("hello") should return False.
Waiting:6. all_unique("freeCodeCamp") should return False.
Waiting:7. all_unique("!@#*$%^&*()aA") should return False.
"""

def all_unique(s):
    for x in range(len(s)):
        for y in range(x + 1, len(s)):
            if s[x]==s[y]:
                return False
    return True

    texto = input
    all_unique(texto)
    

** end of main.py **

