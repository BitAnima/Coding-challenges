"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""


# Definir la función que recibe el string 's'
def solution(s):
    """
    Divide un string en pares de dos caracteres. Si la longitud del string es impar,
    añade un carácter '_' al final para completar el último par.
    Devuelve una lista con todos los pares generados.

    Parámetros:
        s (str): Cadena de texto a dividir.

    Retorna:
        list: Lista de pares de caracteres, cada uno de longitud 2.

    Ejemplos:
        solution('abcdef')  # ['ab', 'cd', 'ef']
        solution('abcde')   # ['ab', 'cd', 'e_']
        solution('')        # []
    """

    # Si el string está vacío, devolver una lista vacía
    if len(s) == 0:
        print(f"La lista está vacía")
        return []

    # Inicializar una lista vacía para guardar los pares de caracteres
    two_characters_chunks = []

    # Si la longitud es impar, añadir un '_' al final del string para emparejarlo
    if len(s) % 2 != 0:
        s = s + '_'

        # Recorrer el string en pasos de 2 y añadir cada par a la lista
    for letter in range(0, len(s), 2):
        two_characters_chunks.append(s[letter:letter + 2])

        # Devolver la lista resultante
    print(two_characters_chunks)
    return two_characters_chunks