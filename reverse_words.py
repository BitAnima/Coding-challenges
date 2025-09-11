"""Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.

1. reverse_sentence("world hello") should return "hello world".
Waiting:2. reverse_sentence("push commit git") should return "git commit push".
Waiting:3. reverse_sentence("npm  install   apt    sudo") should return "sudo apt install npm".
Waiting:4. reverse_sentence("import    default   function  export") should return "export function default import".
"""
"""def reverse_sentence(sentence):

    #Creamos una nueva variable para almacenar la lista de palabras del string
    words_array=[]
    
    #Eliminamos los dobles espacios
    #sentence.replace("  ", "")
    
    #Separamos las palabras del string por espacios y las almacenamos en la lista words_array
    words = sentence.split()#Si no se utiliza nada como separador, los espacios se eliminan
    
    for word in words:
        words_array.append(word)

    De forma más limpia (todo en una línea):
    words_array = sentence.split()
    
    #Imprimimos la cadena original en una sola línea    
    print("Original string:", ' '.join(words_array), "\n")

    #Invertimos el orden de las palabras con el método reverse
    words_array.reverse()
    
    #Imprimimos la cadena invertida en una sola línea
    
    inverted_sentence = ' '.join(words_array)
    print("Inverted string:", inverted_sentence, "\n")
    return inverted_sentence

"""

#Todo el código anterior se podría eliminar y dejar sólo:"""


def reverse_sentence(sentence):
    print("Inverted string:",' '.join(sentence.split()[::-1]), "\n")
    return ' '.join(sentence.split()[::-1])



reverse_sentence("world hello")
reverse_sentence("push commit git")
reverse_sentence("npm  install   apt    sudo")
reverse_sentence("import    default   function  export")

