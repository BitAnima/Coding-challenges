"""
Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first."""

def get_words(paragraph):

    punctuation = ".,!"

    for symbol in punctuation:
        if symbol in paragraph:
            paragraph = paragraph.replace(symbol, "")

    lower_case_words = paragraph.lower()
    words_set = lower_case_words.split()


    words_appearance_dict = {}

    for word in words_set:
        if word in words_appearance_dict:
            words_appearance_dict[word] += 1    
        else:
            words_appearance_dict[word] = 1

    """
    words_appearance_dict.items() crea una lista de tuplas: cada tupla es (palabra, frecuencia).
    El parámetro key=lambda x: x le indica a sorted que debe ordenar usando el “segundo elemento” de cada tupla —es decir,
    la frecuencia con la que aparece cada palabra.
    reverse=True hace que el mayor (la palabra más repetida) quede primero."""
    
    frequency_ordered_list = sorted(words_appearance_dict.items(), key=lambda x: x[1], reverse=True) #CONTIENE TUPLAS. Sin la función lambda se imprimiría una lista alfabética

    # Se crea una lista de compresión con un slicing para tomar sólo los tres primeros elementos
    """La tupla tiene pares asignados. Pair contiene palabra y frecuencia,
    pero pair[0] indica que sólo se debe tomar el primer elemento del par (la palabra)"""
    top_three_words = [pair[0] for pair in frequency_ordered_list[:3]]
    print(top_three_words)
 
    return top_three_words

get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding") # ["coding", "python", "in"].
get_words("I like coding. I like testing. I love debugging!") # ["i", "like", "coding"].
get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!") # ["debug", "test", "deploy"].