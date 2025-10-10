"""Phone Number Formatter
Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD"."""

import re # Importamos el módulo de expresiones regulares

def format_number(number):
    pattern = r'(\d)(\d{3})(\d{3})(\d{4})'
    formatted_number = re.sub(pattern, r'+\1 (\2) \3-\4', number)
    print(formatted_number)
    return formatted_number

    """
    
    **Explicación paso a paso:**
    
    1. **`import re`**: Importa el módulo de expresiones regulares
    
    2. **Patrón `r'(\d)(\d{3})(\d{3})(\d{4})'`**:
       - `(\d)`: Captura 1 dígito (grupo 1) - código de país
       - `(\d{3})`: Captura 3 dígitos (grupo 2) - código de área
       - `(\d{3})`: Captura 3 dígitos (grupo 3) - primeros 3 del número
       - `(\d{4})`: Captura 4 dígitos (grupo 4) - últimos 4 del número
    
    3. **`re.sub(pattern, r'+\1 (\2) \3-\4', number)`**:
       - Sustituye la cadena original con el formato deseado
       - `\1`, `\2`, `\3`, `\4` se refieren a los grupos capturados
       - Resultado: `"+grupo1 (grupo2) grupo3-grupo4"`
       
    
    **Solución sin expresiones regulares**
    
    formatted_number =f"+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:]}"
    print(formatted_number)
    return formatted_number
    """


format_number("05552340182") # "+0 (555) 234-0182".
format_number("15554354792") #"+1 (555) 435-4792".