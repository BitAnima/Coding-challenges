"""
belmud Text
Given a string, return a jumbled version of that string where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.


Waiting:1. jbelmu("hello world") #  "hello wlord".
Waiting:2. jbelmu("i love jumbled text") #  "i love jbelmud text".
Waiting:3. jbelmu("freecodecamp is my favorite place to learn to code") #  "faccdeeemorp is my faiortve pacle to laern to cdoe".
Waiting:4. jbelmu("the quick brown fox jumps over the lazy dog") #  "the qciuk borwn fox jmpus oevr the lazy dog".
"""

def jbelmu(text):

    set_words = text.split()

    print(f"Cadena original: {text}")
    print(f"Palabras originales: {set_words}")

    transformed_words_set = []

    for character in set_words:
        if len(character) <= 2:
            transformed_word = character
            transformed_words_set.append(transformed_word)
            print(f"{transformed_words_set}")
        else:   
            letras_intermedias = sorted(character[1:-1])            
            transformed_word = character[0] +''.join(letras_intermedias) + character[-1]
            transformed_words_set.append(transformed_word)
        
    print(f"Palabras transformadas: {' '.join(transformed_words_set)}\n")

    return ' '.join(transformed_words_set)



transformed_words_set = jbelmu("hello world") #  "hello wlord".
jbelmu("i love jumbled text") #  "i love jbelmud text".
jbelmu("freecodecamp is my favorite place to learn to code") #  "faccdeeemorp is my faiortve pacle to laern to cdoe".
jbelmu("the quick brown fox jumps over the lazy dog") #  "the qciuk borwn fox jmpus oevr the lazy dog".
