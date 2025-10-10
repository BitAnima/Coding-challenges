"""Spam Detector
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:

A represents the country code and can be any number of digits.
BBB represents the area code and will always be three digits.
CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:

The country code is greater than 2 digits long or doesn't begin with a zero (0).
The area code is greater than 900 or less than 200.
The sum of first three digits of the local number appears within last four digits of the local number.
The number has the same digit four or more times in a row (ignoring the formatting characters).
"""

#Importamos módulo para expresiones regulares

import re

# Función para asignar cada parte del número a su código correspondiente. Devuelve las partes como una tupla
def parse_phone_number(phone_number):
   match = re.match(r"\+(\d+)\s+\((\d{3})\) (\d{3})-(\d{4})", phone_number)
   if match:
       return match.groups()
   else:
       return None, None, None, None

#Función que explica los motivos por los que se considera que el número es spam
def provide_reasons(phone_number):
    #Llamada a parse_phone_number y asignación de variables a cada parte
    country_code, area_code, local_area1, local_area2 = parse_phone_number(phone_number)
    print(f"Código de país: {country_code}; código de área: {area_code}; código de área local 1: {local_area1}; código de área local 2: {local_area2}")
    #Lista de motivos vacía
    reasons = []

    # Llamadas a funciones para determinar por qué es spam o no

    #Llamada a función para comprobar el código del país
    if is_not_valid_country_code(country_code):
        reasons.append("El código de país tiene más de dos cifras o comienza por algún número distinto de 0.")

    # Llamada a función para comprobar el código de área
    if is_not_valid_area_code(area_code):
        reasons.append("El código de área es mayor de 900 o menor de 200.")

    # Llamada a función para comprobar si la suma de los primeros tres números del código de área local 1 aparece como secuencia en la cadena de números de área local 2
    if is_sum_local_area1_in_local_area2(local_area1, local_area2):
        reasons.append("La suma de los primeros tres números del código de área local 1 aparece como secuencia en la cadena de números de área local 2.")

    # Llamada a función para comprobar si el número de teléfono tiene el mismo dígito cuatro o más veces.
    clean_string = clean_not_numbers(phone_number)
    if is_digit_4times_repeated(clean_string):
        reasons.append("Uno de los dígitos aparece repetido cuatro veces o más.")



    return reasons



# Función para determinar si el código de área tiene más de 2 dígitos o comienza por algún número distinto de 0
def is_not_valid_country_code(country_code):
    #Evaluamos si el código de país tiene más de 2 números
    if len(country_code) > 2 or not country_code.startswith("0"):
        return True
    return False

# Función para determinar si el código de área es mayor de 900 o menor de 200
def is_not_valid_area_code(area_code):
    int_area_code = int(area_code) # Hay que convertir la cadena a un entero para que funcione
    if int_area_code < 200 or int_area_code > 900:
        return True
    return False

#Función para determinar si la suma del área local 1 está contenida en el área local 2
def is_sum_local_area1_in_local_area2(local_area1, local_area2):
    sum_local_area1 = sum(int(digit) for digit in local_area1) # Se suman los dígitos como enteros y luego se convierte todo a una cadena
    return str(sum_local_area1) in local_area2 # Se comprueba si la cadena está contenida en la otra y devuelve True o False

# Llamada para determinar si un dígito se repite cuatro veces o más
def is_digit_4times_repeated(clean_string):
    for i in range(len(clean_string) - 3): # Debemos añadir -3 para que el bucle no se salga del rango
        if clean_string[i] == clean_string[i+1] == clean_string[i+2] == clean_string[i+3]:
            return True
    return False



# Función para eliminar los caracteres no numéricos del string
def clean_not_numbers(phone_number):
    clean_string = re.sub(r'\D', '', phone_number)
    print(f"Número sin caracteres no numéricos: {clean_string}")
    return clean_string

# Función que determina si hay números repetidos en la cadena




#Función que determina si un número es spam haciendo llamadas a otras funciones

def is_spam(number):
    # Llamada a función para dar motivos sobre si es spam o no
    resultados = provide_reasons(number)

    # Si la lista de razones está vacía, el número no es spam
    if len(resultados) > 0:
        print(f"El número {number} es spam.")
        print(f"Razones por las que es spam:")
        for razones in resultados:
            print(f"- {razones}")
        return True
    else:
        print(f"El número {number} no es spam.")
        return False

    # LLamada a función para limpiar caracteres no numéricos
    clean_not_numbers(number)

    return number


is_spam("+0 (200) 234-0182") # False.
is_spam("+091 (555) 309-1922") # True.
is_spam("+1 (555) 435-4792") # True.
is_spam("+0 (955) 234-4364") # True.
is_spam("+0 (155) 131-6943") # True.
is_spam("+0 (555) 135-0192") # True.
is_spam("+0 (555) 564-1987") # True.
is_spam("+00 (555) 234-0182") # False.