"""P@ssw0rd Str3ngth!
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

It is at least 8 characters long.
It contains both uppercase and lowercase letters.
It contains at least one number.
It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium"
if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules."""

import re

def check_strength(password):
    number_of_rules_met = 0

    if len(password) > 8:
        number_of_rules_met += 1

    if re.search(r"[a-z]", password) is not None and re.search(r"[A-Z]", password) is not None:
        number_of_rules_met += 1

    if re.search(r'[!, @, #, $, %, ^, &, *]', password) is not None:
        number_of_rules_met += 1

    if re.search(r"[0-9]", password) is not None:
        number_of_rules_met += 1

    print(number_of_rules_met)

    if number_of_rules_met  < 2:
        print("weak")
        return "weak"
    if 2 <= number_of_rules_met < 4:
        print("medium")
        return "medium"
    if number_of_rules_met >= 4:
        print("strong")
        return "strong"

check_strength("123456") # "weak".
check_strength("pass!!!") # "weak".
check_strength("Qwerty") # "weak".
check_strength("PASSWORD") # "weak".
check_strength("PASSWORD!") # "medium".
check_strength("PassWord%^!") # "medium".
check_strength("qwerty12345") # "medium".
check_strength("PASSWORD!") # "medium".
check_strength("PASSWORD!") # "medium".
check_strength("S3cur3P@ssw0rd") # "strong".
check_strength("C0d3&Fun!") # "strong".