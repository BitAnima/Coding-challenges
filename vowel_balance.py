"""
Vowel Balance
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

Waiting:1. is_balanced("racecar") # True.
Waiting:2. is_balanced("Lorem Ipsum") # True.
Waiting:3. is_balanced("Kitty Ipsum") # False.
Waiting:4. is_balanced("string") # False.
Waiting:5. is_balanced(" ") # True.
Waiting:6. is_balanced("abcdefghijklmnopqrstuvwxyz") # False.
Waiting:7. is_balanced("123A#b!E&*456-o.U") # True.
"""

def is_balanced(s):

    print(f"Cadena original: {s}\n")

    vowels_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"} #Las vocales se almacenan en un set porque es más eficiente (no hace falta recorrer toda la lista)

    longitud = len(s)
    caracter_mitad = longitud // 2 #División entera

    if longitud % 2 == 0:
        mitad1 = s[:caracter_mitad]
        mitad2 = s[caracter_mitad:]
        print(f"Mitades: {mitad1}, {mitad2}")

    else:
        mitad1 = s[:caracter_mitad+1]
        mitad2 = s[caracter_mitad:]
        print(f"Mitades: {mitad1}, {mitad2}")
 
    contador_mitad1 = 0
    contador_mitad2 = 0

    for letra in mitad1:
        if letra in vowels_set:
            contador_mitad1 += 1
            print(f"Mitad 1 - Vocales encontradas: {letra}")

    for letra in mitad2:
        if letra in vowels_set:
            contador_mitad2 += 1
            print(f"Mitad 2 - Vocales encontradas: {letra}")
    
    print(f"\nEl resultado del recuento ha sido: Mitad 1 -> {contador_mitad1}; Mitad 2 -> {contador_mitad2}\n")
    if contador_mitad1 == contador_mitad2:
        print(f"Las dos mitades tienen el mismo número de vocales.\n")
    else:
        print(f"Las mitades tienen distinto número de vocales.\n")
            
    return contador_mitad1 == contador_mitad2

is_balanced("racecar") # True.
is_balanced("Lorem Ipsum") # True.
is_balanced("Kitty Ipsum") # False.
is_balanced("string") # False.
is_balanced(" ") # True.
is_balanced("abcdefghijklmnopqrstuvwxyz") # False.
is_balanced("123A#b!E&*456-o.U") # True.