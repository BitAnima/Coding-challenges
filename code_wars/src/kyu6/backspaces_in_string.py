"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.

Examples
"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""
"""


def clean_string(s):
    new_string = []

    for character in s:
        if character != '#':
            new_string.append(character)
        if character == '#':
            if len(new_string) > 0:
                new_string.pop()

    print(new_string)
    return ''.join(new_string)

