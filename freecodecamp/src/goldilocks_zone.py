"""
Space Week Day 5: Goldilocks Zone

Este módulo permite calcular los límites de la "zona Goldilocks" (zona habitable)
alrededor de una estrella, dados su masa relativa al Sol.

Funciones:
    - goldilocks_zone(mass): Devuelve el rango [inicio, fin] en unidades astronómicas
      donde puede existir agua líquida.
    - calculate_luminosity(mass): Calcula la luminosidad relativa a partir de la masa.
    - calculate_start_and_end_zone(luminosity): Calcula los límites de la zona habitable
      usando la luminosidad.

Excepciones:
    - ValueError: Si la masa es menor o igual que cero.

Este archivo puede ser probado con test_goldilocks_zone.py.
"""


import math

# Paso 1: Calcular luminosidad

def calculate_luminosity(mass: float) -> float:
    """
      Calcula la luminosidad de una estrella a partir de su masa relativa al Sol.

      Parámetros:
          mass (float): Masa de la estrella (relativa al Sol).

      Devuelve:
          float: Luminosidad calculada según la fórmula mass ** 3.5.
      """
    luminosity = pow(mass, 3.5)
    return luminosity

# Paso 2: Calcular la raíz cuadrada de luminosidad
# Paso 3: Calcular inicio y fin con las fórmulas

def calculate_start_and_end_zone(luminosity: float) -> tuple[float, float]:
    """
       Calcula los límites de la zona habitable (zona Goldilocks) utilizando la luminosidad.

       Parámetros:
           luminosity (float): Luminosidad de la estrella.

       Devuelve:
           tuple[float, float]: Tuple (inicio, fin) no redondeados, en Unidades Astronómicas.
       """
    start_zone = math.sqrt(luminosity) * 0.95
    end_zone = math.sqrt(luminosity) * 1.37
    return start_zone, end_zone

# Paso 4: Redondear ambos al segundo decimal
# Paso 5: Devolver como lista

def goldilocks_zone(mass: float) -> list[float]:
    """
    Devuelve el rango de la zona Goldilocks de una estrella, con dos decimales de precisión.

    Parámetros:
        mass (float): Masa de la estrella (mayor a 0), relativa al Sol.

    Devuelve:
        list[float]: Lista [inicio, fin] de la zona habitable, redondeados a dos decimales
          en Unidades Astronómicas.

    Lanza:
        ValueError: Si mass es menor o igual que 0.
    """
    if mass > 0:
        luminosity = calculate_luminosity(mass)
        start_zone, end_zone = calculate_start_and_end_zone(luminosity)

        return [round(start_zone, 2), round(end_zone, 2)]
    else:
        raise ValueError("La masa debe ser positiva")