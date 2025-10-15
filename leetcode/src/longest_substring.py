"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without duplicate characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces."""


def lengthOfLongestSubstring(s: str = "aabbccdd") -> int:
        start = 0
        longest = 0
        current_substring = {}

        for end, char in enumerate(s):
            if char in current_substring and current_substring[char] >= start:
                # Sliding window: Si el caracter se encuentra entre los que ya se han registrado anteriormente, se avanza una posición
                start = current_substring[char] + 1
            current_substring[char] = end # Actualizamos el diccionario con el nuevo caracter
            longest = max(longest, end - start + 1)
            #print(f"{char=}, {start=}, {end=}, {longest=}, {current_substring}")

        #print(longest)
        return longest


lengthOfLongestSubstring()

"""Esquema profesional (sin solución directa):
Usa dos punteros (start, end) para definir los límites de la ventana actual.

Utiliza un conjunto o diccionario para saber qué caracteres han aparecido en la ventana.

Recorre el string:

Si el carácter no está en el conjunto, amplía la ventana (mueve end a la derecha, añade el carácter al set y actualiza la longitud máxima).

Si el carácter ya está en el conjunto, saca caracteres desde la izquierda (avanza start) hasta que el duplicado desaparezca.

Devuelve la longitud máxima obtenida.

Ejemplo de pseudocódigo:
python
max_length = 0
start = 0
used_chars = {}

for end, char in enumerate(s):
    if char in used_chars and used_chars[char] >= start:
        start = used_chars[char] + 1
    used_chars[char] = end
    max_length = max(max_length, end - start + 1)
Detalles profesionales:

used_chars guarda la última posición vista de cada carácter.

Cuando hay un duplicado, mueve start justo después de la posición anterior del carácter duplicado, ¡no solo +1!

Es O(n), muy eficiente para strings largos."""