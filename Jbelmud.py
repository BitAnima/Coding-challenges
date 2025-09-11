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

    print("\n")
    print(f"Cadena original: {text}")
    print(f"Palabras originales: {set_words}")

    for character in set_words:
        letras_intermedias = sorted(character[1:-1])
        #print(f"{''.join(letras_intermedias)}")
        
        print(f"{character[0]}{''.join(letras_intermedias)}{character[-1]}")



    print("\n")

    #return text

jbelmu("hello world") #  "hello wlord".
# jbelmu("i love jumbled text") #  "i love jbelmud text".
# jbelmu("freecodecamp is my favorite place to learn to code") #  "faccdeeemorp is my faiortve pacle to laern to cdoe".
# jbelmu("the quick brown fox jumps over the lazy dog") #  "the qciuk borwn fox jmpus oevr the lazy dog".
