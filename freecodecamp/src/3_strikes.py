"""
3 Strikes
Given an integer between 1 and 10,000, return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
"""

"""
***************************************************************************
La Solución recursiva NO FUNCIONA porque hace demasidas llamadas recursivas
***************************************************************************

def squares_with_three(n):
    lista_cuadrados = []

    def recursivo(j):
        if j == 1:
            cuadrado = pow(1, 2)
            lista_cuadrados.append(cuadrado)
            return
        else:
            recursivo(j - 1)
            cuadrado = pow(j, 2)
            lista_cuadrados.append(cuadrado)
            return

    recursivo(n)

    count = 0
    for number in lista_cuadrados:
        # Revisar si el dígito '3' está presente en el cuadrado
        if '3' in str(number):
            count += 1
    return count
    """

def squares_with_three(n):

    lista_cuadrados = []
    count = 0

    for number in range(n, 0, -1): # desde n hasta 1, descendente
        cuadrado = pow(number, 2)
        lista_cuadrados.append(cuadrado)

    for number in lista_cuadrados:
        if '3' in str(number):
            count += 1
    print(f"Recuento de cuadrados con el número 3: {count}")
    return count

"""
Versión reducida:
def squares_with_three(n):
    count = 0
    for number in range(n, 0, -1):
        if '3' in str(number ** 2):
            count += 1
    return count
"""


squares_with_three(1) #  0.
squares_with_three(10) #  1.
squares_with_three(100) #  19.
squares_with_three(1000) #  326.
squares_with_three(10000) #  4531.