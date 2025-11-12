""""HTML Tag Stripper
Given a string of HTML code, remove the tags and return the plain text content.

The input string will contain only valid HTML.
HTML tags may be nested.
Remove the tags and any attributes.
For example, '<a href="#">Click here</a>' # "Click here"."""

def strip_tags(html: str) -> str:

    html_str = ""
    in_tag = False
    for character in html:
        if character == '<': # Al encontrar '<' se activa la bandera
            in_tag = True
        elif character == '>': # Aquí se desactiva
            in_tag = False
        elif not in_tag:
            html_str += character # Sólo se copian los caracteres que no estén dentro de la bandera
    # Este sí es texto visible
    print(html_str)
    return html_str

strip_tags('<a href="#">Click here</a>') # "Click here".
strip_tags('<p class="center">Hello <b>World</b>!</p>') # "Hello World!".
strip_tags('<img src="cat.jpg" alt="Cat">') # an empty string ("").
strip_tags('<main id="main"><section class="section">section</section><section class="section">section</section></main>') # sectionsection