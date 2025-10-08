"""
Perfect Square
Given an integer, determine if it is a perfect square.

A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
"""

import math

def is_perfect_square(n):

    """"if math.sqrt(abs(n) * math.sqrt(abs(n) == n:"""
    absolute_value = abs(n)

    if int(math.sqrt(absolute_value)) * int(math.sqrt(absolute_value)) == int(n):
        print(f"Perfect Square: {int(math.sqrt(absolute_value) * math.sqrt(absolute_value))}")
        return True
    else:
        print(f"Not a Perfect Square: {int(math.sqrt(absolute_value) * math.sqrt(absolute_value))}")
        return False

is_perfect_square(9) # True.
is_perfect_square(49) # True.
is_perfect_square(1) # True.
is_perfect_square(2) # False.
is_perfect_square(99) # False.
is_perfect_square(-9) # False.
is_perfect_square(0) # True.
is_perfect_square(25281) # True.