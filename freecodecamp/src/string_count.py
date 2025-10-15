"""String Count
Given two strings, determine how many times the second string appears in the first.

The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two."""

def count(text, parameter):

    counter = 0

    for char in range(0, len(text) - len(parameter) + 1):
        if text[char:char+len(parameter)] == parameter:
            counter += 1
    print(counter)

    return counter

counter = count('abcdefg', 'def')