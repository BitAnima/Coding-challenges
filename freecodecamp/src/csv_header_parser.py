"""CSV Header Parser
Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

The first line of a CSV file contains headings separated by commas.
Remove any leading or trailing whitespace from each heading."""
import csv


def get_headings(csv):
    headings = []
    raw_headings = csv.split(',')
    print(raw_headings)

    for heading in raw_headings:
        headings.append(heading.strip())
    # print(headings)
    return headings




"""¡Claro! Aquí tienes un ejemplo de código que **hace algo similar** pero no es exactamente igual al reto. Así puedes ver la lógica general sin copiar la solución:

```python
# Supón que tienes una lista de nombres separados por punto y coma, y quieres limpiarlos
def limpiar_nombres(cadena):
    partes = cadena.split(';')  # Separar usando punto y coma
    nombres_limpios = []
    for nombre in partes:
        nombres_limpios.append(nombre.strip())  # Quitar espacios
    return nombres_limpios

# Ejemplo de uso:
print(limpiar_nombres(" Ana ; Juan ;  Pedro "))  # ['Ana', 'Juan', 'Pedro']
```

**¿Qué puedes aprender de este ejemplo?**
- Cambia el separador (`;` por `,`) según lo que necesites.
- Usa `.split()` para separar la cadena.
- Usa `.strip()` para limpiar cada elemento.
- Puedes usar una lista por comprensión para hacerlo en una sola línea si quieres practicar.

¿Te gustaría intentar adaptar este ejemplo al reto, o necesitas otra pista sobre cómo hacerlo con comas y encabezados?

[1](https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-28)"""

get_headings("name,age,city") # ["name", "age", "city"].
get_headings("first name,last name,phone") # ["first name", "last name", "phone"].
get_headings("username , email , signup date ") # ["username", "email", "signup date"].