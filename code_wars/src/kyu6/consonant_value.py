"""
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.
Consonants are any letters of the alphabet except "aeiou".
We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
For example, for the word "zodiac", let's cross out the vowels. We get: "z o d ia c"
"zodiac" -> 26
The consonant substrings are: "z", "d" and "c" with values "z" = 26, "d" = 4 and "c" = 3. The highest is 26.
"strength" -> 57
The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.
For C: do not mutate input.
"""

def solve(s = "zodiac"):
    max_value = 0
    current_value = 0

    for char in s:
        if char.isalpha and char not in "aeiou":
            current_value += ord(char) - ord('a') + 1
            print(f"{char} -> {current_value}")
        else:
            if current_value > max_value:
                max_value = current_value
            current_value = 0
    if current_value > max_value:
        max_value = current_value

    result = max_value
    print(f"Valor máximo: {result}")
    return result

solve("chruschtschov")

"""
Solución con expresiones regulares:
import re

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))
"""