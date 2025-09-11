"""Roman Numeral Parser
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added."""


def parse_roman_numeral(numeral):

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    valor_actual = numeral[0]
    total = 0
    

    for posicion in range(len(numeral)):
        valor_actual = roman_dict[numeral[posicion]]
        print(f"\nNúmero romano: {numeral}")
        print(f"letra romana: {numeral[posicion]} = valor asignado: {valor_actual}")
        print(f"Posición actual: {posicion}")
        print(f"Total actual: {total}")
              
        if posicion + 1 < len(numeral):
            siguiente_letra = roman_dict[numeral[posicion + 1]]
            
            if valor_actual < siguiente_letra:                
                print(f"El valor actual ({valor_actual}) es menor que el siguiente valor ({siguiente_letra}), por lo que se resta.")
                total -= valor_actual

            else:                
                print(f"El valor actual ({valor_actual}) es mayor o igual que el siguiente valor ({siguiente_letra}), por lo que se suma.")
                total += valor_actual
        else:
            print(f"Última letra romana, se suma el valor actual ({valor_actual}) al total ({total}).")
            total += valor_actual
            

    print(f"El valor total de {numeral} es {total}")
    return total

parse_roman_numeral("XIV")
parse_roman_numeral("XCIX")
parse_roman_numeral("CDLX")
parse_roman_numeral("MMXXV")