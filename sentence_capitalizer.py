"""Sentence Capitalizer
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.
All other characters should be preserved.
Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!)."""

import re

def capitalize(paragraph):
    partes = re.split(r'([.!?]+)', paragraph)
    
    nueva_frase = []
    capitalizar = True  # Empezamos capitalizando la primera parte

    for word in partes:
        if word.strip() == '':  # Si el fragmento está vacío o solo contiene espacios, se ignora.
            continue
        if capitalizar:  # Si debemos capitalizar la siguiente frase
            """
            ¿Qué está pasando aquí?
            - enumerate(word) recorre cada carácter c del fragmento word, junto con su posición i.
            - if c.isalpha() verifica si ese carácter es una letra (no espacio, número, símbolo, etc.).
            - Cuando encuentra la primera letra, hace lo siguiente:
            - word[:i]: toma todo lo que hay antes de esa letra.
            - c.upper(): convierte esa letra a mayúscula.
            - word[i+1:]: toma todo lo que hay después de esa letra.
            - Luego une todo eso en una nueva versión de word.
            - break: rompe el bucle inmediatamente después de capitalizar solo esa primera letra.
            """
            for i, c in enumerate(word):  # Recorremos cada carácter y su posición en el fragmento
                if c.isalpha():           # Si encontramos la primera letra (carácter alfabético)
                    word = word[:i] + c.upper() + word[i+1:]  # La cambiamos a mayúscula, conservando el resto igual
                    break                 # Solo cambiamos la primera letra, luego salimos del bucle
            nueva_frase.append(word)      # Añadimos el fragmento (ya capitalizado) a la lista resultado
            capitalizar = False           # Ya hemos capitalizado, así que desactivamos la bandera hasta el próximo signo
        else:
            nueva_frase.append(word)      # Si no se debe capitalizar, agregamos el fragmento tal cual

        # Si word es solo signos (., !, ?), la siguiente parte hay que capitalizarla
        if re.fullmatch(r'[.!?]+', word):
            capitalizar = True

    print(f"{''.join(nueva_frase)}")

    return ''.join(nueva_frase)


capitalize("this is a simple sentence.") # "This is a simple sentence.".
capitalize("hello world. how are you?") # "Hello world. How are you?".
capitalize("i did today's coding challenge... it was fun!!") # "I did today's coding challenge... It was fun!!".
capitalize("crazy!!!strange???unconventional...sentences.") # "Crazy!!!Strange???Unconventional...Sentences.".
capitalize("there's a space before this period . why is there a space before that period ?") # "There's a space before this period . Why is there a space before that period ?".