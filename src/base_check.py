"""Base Check
Given a string representing a number, and an integer base from 2 to 36, determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z"""

def is_valid_number(n, base):
    #Pasamos todos los caracteres a mayúsculas
    cadena = n.upper()

    for character in cadena:
        #Si el caracter es un número, se devuelve directamente el valor del número
        if character.isdigit():
            valor = int(character) #convertimos el caracter a un entero
            #print(f"{valor}")
            """
        Si el caracter es una letra, hay que calcular su valor con la función ord,
        que sirve para obtener el valor numérico Unicode (código ASCII) de un carácter.
        ¿Qué hace ord('C')?
        Da el código numérico de la letra 'C' en ASCII/Unicode: ord('C')  # Devuelve 67
        ¿Por qué le restamos ord('A')? Porque así calculamos la diferencia entre ellos,
        o sea, cuántas posiciones hay desde 'A': ord('C') - ord('A')  # 67 - 65 = 2
        ¿Por qué le sumamos 10 al resultado? Porque en base 16, la letra 'A' corresponde al número 10, 'B' al 11, 'C' al 12...
        Así que: ord('C') - ord('A') + 10  # 2 + 10 = 12
        """
        
        #Usamos elif character.isalpha() en vez de un segundo if separado para que solo se ejecute si el carácter no era un dígito.

        elif character.isalpha():
            valor = ord(character) - ord('A') + 10
            print(f"{ord(character)} - {ord('A')} + 10 = {valor}")

        else:
            print(f"False")
            return False
        
        if  valor >= base:
            print(f"False")
            return False
        
        
                
    
    print(f"True") # Si se pasan todas las comprobaciones
    return True
    

is_valid_number("10101", 2) # True.
is_valid_number("10201", 2) # False.
is_valid_number("76543210", 8) # True.
is_valid_number("9876543210", 8) # False.
is_valid_number("9876543210", 10) # True.
is_valid_number("ABC", 10) # False.
is_valid_number("ABC", 16) # True.
is_valid_number("Z", 36) # True.
is_valid_number("ABC", 20) # True.
is_valid_number("4B4BA9", 16) # True.
is_valid_number("5G3F8F", 16) # False.
is_valid_number("5G3F8F", 17) # True.
is_valid_number("abc", 10) # False.
is_valid_number("abc", 16) # True.
is_valid_number("AbC", 16) # True.
is_valid_number("z", 36) # True.