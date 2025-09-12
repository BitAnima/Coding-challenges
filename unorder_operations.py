"""
Unorder of Operations
Given an array of integers and an array of string operators, apply the operations to the numbers sequentially from left-to-right. Repeat the operations as needed until all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

Valid operators are +, -, *, /, and %.
"""
import operator # Para convertir strings como "+" o "*" en operadores en Python, se puede usar la librería estándar operator, que incluye funciones para cada operación básica

def evaluate(numbers, operators):
    op_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv,  # división entera como indica el enunciado con enteros
        '%': operator.mod
    }
    result = numbers[0]
    n = len(numbers)
    m = len(operators)
    for i in range(1, n):
        # Usamos el operador en la posición cíclica correspondiente
        op_func = op_map[operators[(i-1)%m]] # el operador % es el operador módulo en Python, y m es la cantidad de operadores en la lista operators.
        
        """¿Qué hace (i-1) % m?
        Sirve para que, al avanzar por la lista de números, puedas usar los operadores de manera cíclica.
        Si hay más números que operadores, los operadores se reutilizan desde el principio."""

        result = op_func(result, numbers[i])
        print(f"{result}")
    return result


# print(evaluate([1, 2, 3, 4, 5], ['+', '*']))  # Imprime 27, porque (1+2)*3+4*5 = 27 con evaluación estrictamente izquierda a derecha


evaluate([5, 6, 7, 8, 9], ['+', '-']) #  3
evaluate([17, 61, 40, 24, 38, 14], ['+', '%']) #  38
evaluate([20, 2, 4, 24, 12, 3], ['*', '/']) #  60
evaluate([11, 4, 10, 17, 2], ['*', '*', '%']) #  30
evaluate([33, 11, 29, 13], ['/', '-']) #  -2