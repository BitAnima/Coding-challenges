"""
Message Decoder
Given a secret message string, and an integer representing the number of letters
that were used to shift the message to encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded."""

def decode(message, shift):
    decoded_message = ""

    for character in message:
        if character.isalpha():
            if character.isupper():
                base = ord('A')
            else:
                base = ord('a')

            shifted = (ord(character) - base - shift) % 26 + base
            """Se calcula según los caracteres Unicode/ASCII.
             Se resta la base (el valor de la letra a en mayúscula o minúscula)
             y se resta el número de posiciones que se ha desplazado la letra.
             Com módulo 26 (% 26) se consigue que la iteración no se salga del rango (26 letras del alfabeto)."""
            decoded_message += chr(shifted)
        else:
            decoded_message += character #Para el resto de caracteres que no cambian

    print(f"{decoded_message}")
    return decoded_message

decode("Xlmw mw e wigvix qiwweki.", 4) #  "This is a secret message."
decode("Byffi Qilfx!", 20) #  "Hello World!"
decode("Zqd xnt njzx?", -1) #  "Are you okay?"
decode("oannLxmnLjvy", 9) #  "freeCodeCamp"