"""
Factorializer
Given an integer from zero to 20, return the factorial of that number. The factorial of a number is the product of all the numbers between 1 and the given number.

The factorial of zero is 1.

Waiting:1. factorial(0) should return 1.
Waiting:2. factorial(5) should return 120.
Waiting:3. factorial(20) should return 2432902008176640000.
"""

# Solución iterativa:

def factorial(n):

    resultado = 1

    print(f"\nValor original: {n}")

    if n == 0:
        resultado = 1
        print(f"Resultado: {resultado}\n")
    else:
        for precedent_number in range(1, n+1):
            resultado *= precedent_number
            print(f"Multiplicando por {precedent_number}. Resultado: {resultado}")        

    return resultado

factorial(0)  # 1.
factorial(5)  # 120.
factorial(20)  # 2432902008176640000.


"""
Solución recursiva:

def factorial(n):
    def recursivo(k):
        if k == 0:
            return 1, []
        else:
            parcial, pasos = recursivo(k - 1)
            resultado = k * parcial
            pasos.append(str(k))
            print(f"Multiplicando por {k}. Resultado: {resultado}")
            return resultado, pasos

    print(f"\nValor original: {n}")
    resultado, cadena = recursivo(n)
    cadena_str = " × ".join(cadena)
    
    return resultado, cadena_str
    
resultado, cadena = factorial(5)
print(f"\nCálculo completo: {cadena} = {resultado}\n")
"""





