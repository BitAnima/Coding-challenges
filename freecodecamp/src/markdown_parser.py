"""
Markdown Image Parser
Given a string of an image in Markdown, return the equivalent HTML string.

A Markdown image has the following format: "![alt text](image_url)". Where:

alt text is the description of the image (the alt attribute value).
image_url is the source URL of the image (the src attribute value).
Return a string of the HTML img tag with the src set to the image URL and the alt set to the alt text.

For example, given "![Cute cat](cat.png)" return '<img src="cat.png" alt="Cute cat">';
"""

def parse_image(markdown):

    start_url = markdown.index('(') + 1
    end_url = markdown.index(')')
    img_url = markdown[start_url:end_url]

    alt_text_start = markdown.index('[') +1
    alt_text_end = markdown.index(']')
    alt_text = markdown[alt_text_start:alt_text_end]

    print(f'<img src="{img_url}" alt="{alt_text}">')
    return f'<img src="{img_url}" alt="{alt_text}">'




    return markdown

parse_image("![Cute cat](cat.png)") #'<img src="cat.png" alt="Cute cat">'.
parse_image("![Rocket Ship](https://freecodecamp.org/cdn/rocket-ship.jpg)") #'<img src="https://freecodecamp.org/cdn/rocket-ship.jpg" alt="Rocket Ship">'.
parse_image("![Cute cats!](https://freecodecamp.org/cats.jpeg)") #'<img src="https://freecodecamp.org/cats.jpeg" alt="Cute cats!">'.