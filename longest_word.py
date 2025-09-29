"""Longest Word
Given a sentence, return the longest word in the sentence.

Ignore periods (.) when determining word length.
If multiple words are ties for the longest, return the first one that occurs."""

def get_longest_word(sentence):

    word_lengths_dict = {}
    for word in sentence.split():
        word = word.replace(".", "")
        word_lengths_dict[word] = len(word)

    longest_word = max(word_lengths_dict, key=word_lengths_dict.get) # Devuelve la clave con valor máximo

    print(word_lengths_dict)
    print(longest_word)


    return longest_word

    """
    Solución más compacta:
    
    def get_longest_word(sentence):
    # 1. Crear lista de palabras y eliminar puntos
    words = [word.replace(".", "") for word in sentence.split()]
    
    # 2. Encontrar la palabra más larga
    # Si hay empate, max() devuelve la primera que encuentra
    longest_word = max(words, key=len)
    
    return longest_word

    """

get_longest_word("coding is fun") # "coding".
get_longest_word("Coding challenges are fun and educational.") # "educational".
get_longest_word("This sentence has multiple long words.") # "sentence".