"""
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers."""

def is_unnatural_prime(n):

    num = abs(n)
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

is_unnatural_prime(1) # False.
# is_unnatural_prime(-1) # False.
# is_unnatural_prime(19) # True.
# is_unnatural_prime(-23) # True.
# is_unnatural_prime(0) # False.
# is_unnatural_prime(97) # True.
# is_unnatural_prime(-61) # True.
# is_unnatural_prime(99) # False.
# is_unnatural_prime(-44) # False.