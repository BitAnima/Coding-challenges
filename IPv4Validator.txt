** start of main.py **

""""IPv4 Validator
Given a string, determine if it is a valid IPv4 Address. A valid IPv4 address consists of four integer numbers separated by dots (.). Each number must satisfy the following conditions:

It is between 0 and 255 inclusive.
It does not have leading zeros (e.g. 0 is allowed, 01 is not).
Only numeric characters are allowed."""


def is_valid_ipv4(ipv4):
    numbers = ipv4.split('.')

    # Deben ser exactamente 4 bloques y ninguno vacío
    if len(numbers) != 4 or any(n == "" for n in numbers):
        return False

    for number in numbers:
        # Chequeo de sólo dígitos y sin ceros a la izquierda
        if not number.isdigit() or (len(number) > 1 and number[0] == '0'):
            return False
        n = int(number)
        if n < 0 or n > 255:
            return False

    return True


** end of main.py **

