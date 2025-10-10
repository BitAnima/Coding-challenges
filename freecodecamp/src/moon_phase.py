"""Instructions
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.
"""
from datetime import datetime, date

def parse_date_string(date_string) -> date:
    """Parse a date string into a date object.
    """
    date = datetime.strptime(date_string, "%Y-%m-%d")

    # Extraer componentes
    year = date.year  # numérico (int)
    month = date.month  # numérico (int)
    day = date.day  # numérico (int)
    print(year, month, day)   # Resultado: 2000 1 13
    return year, month, day


def is_leap_year(year):
    """Regla general para los años bisiestos:
        Un año es bisiesto si es divisible entre 4.
        Pero… si el año también es divisible entre 100, entonces NO es bisiesto, a menos que…
        …el año sea divisible entre 400. En ese caso, sí es bisiesto.
        En resumen:
        Si el año se puede dividir entre 4 → podría ser bisiesto.
        Si el año, además, se puede dividir entre 100 → ya NO es bisiesto, salvo que…
        Si el año, además, se puede dividir entre 400 → SÍ es bisiesto.
        Ejemplos:
        2024: divisible entre 4 → bisiesto.
        1900: divisible entre 4 y entre 100, pero NO entre 400 → no es bisiesto.
        2000: divisible entre 4, entre 100 y entre 400 → sí es bisiesto."""

    leap_year = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
    print(leap_year)
    return leap_year



def calculate_days_spent(year, month, day):
    reference_year, reference_month, reference_day = 2000, 1, 6
    days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    total_days = 0

    # Sumar los días de los años completos desde la referencia hasta el año actual (excluyendo año actual):
    for y in range(reference_year, year):
        total_days += 366 if is_leap_year(y) else 365

    # Sumar los días de meses completos del año actual:
    for m in range(1, month):
        if m == 2 and is_leap_year(year):
            total_days += 29
        else:
            total_days += days_per_month[m]

    # Sumar los días del mes actual
    total_days += day

    # Restar los días del mes de referencia
    total_days -= reference_day

    print(f"Total days spent: {total_days}")
    return total_days



def moon_phase(date_string):
    year, month, day = parse_date_string(date_string)
    days_spent = calculate_days_spent(year, month, day)
    cycle_day = (days_spent % 28) + 1
    if 1 <= cycle_day <= 7:
        print("New moon")
        return "New"
    elif 8 <= cycle_day <= 14:
        print("Waning")
        return "Waxing"
    elif 15 <= cycle_day <= 21:
        print("Full")
        return "Full"
    elif 22 <= cycle_day <= 28:
        print("Waning")
        return "Waning"

"""
Código más sencillo en el que no hace falta calcular si el año es bisiesto

def moon_phase(date_string):
    # Definir la fecha de referencia
    ref_date = datetime.strptime("2000-01-06", "%Y-%m-%d").date()
    # Convertir la fecha dada a objeto date
    given_date = datetime.strptime(date_string, "%Y-%m-%d").date()

    # Calcular los días transcurridos desde la referencia
    days_passed = (given_date - ref_date).days

    # Día dentro del ciclo lunar (del 1 al 28)
    cycle_day = (days_passed % 28) + 1

    if 1 <= cycle_day <= 7:
        return "New"
    elif 8 <= cycle_day <= 14:
        return "Waxing"
    elif 15 <= cycle_day <= 21:
        return "Full"
    elif 22 <= cycle_day <= 28:
        return "Waning"""