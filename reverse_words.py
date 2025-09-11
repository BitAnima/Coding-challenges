"""Reverse Sentence
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.

1. reverse_sentence("world hello") should return "hello world".
Waiting:2. reverse_sentence("push commit git") should return "git commit push".
Waiting:3. reverse_sentence("npm  install   apt    sudo") should return "sudo apt install npm".
Waiting:4. reverse_sentence("import    default   function  export") should return "export function default import".
"""
def reverse_sentence(sentence):

    words_array=[]
    
    words = sentence.split(' ')
    for word in words:
        print(f"{word}")
        words_array.append(word)
        print(f"{words_array}")   

    #inverted_sentence = print(f"{word[i]} ")

    #return inverted_sentence


reverse_sentence("world hello")
#reverse_sentence("push commit git")
#reverse_sentence("npm  install   apt    sudo")
#reverse_sentence("import    default   function  export")