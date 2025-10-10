"""Array Duplicates
Given an array of integers, return an array of integers that appear more than once in the initial array, sorted in ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.
Run the Tests (Ctrl + Enter)
Reset this lesson
Get Help
Tests
Waiting:1. find_duplicates([1, 2, 3, 4, 5]) should return [].
Waiting:2. find_duplicates([1, 2, 3, 4, 1, 2]) should return [1, 2].
Waiting:3. find_duplicates([2, 34, 0, 1, -6, 23, 5, 3, 2, 5, 67, -6, 23, 2, 43, 2, 12, 0, 2, 4, 4]) should return [-6, 0, 2, 4, 5, 23]."""

def find_duplicates(arr):
    # Creamos un diccionario vacío para contar cuántas veces aparece cada número del array
    contador = {}

    # Recorremos cada elemento del array original
    for elemento in arr:
        # Si el elemento ya está en el diccionario, sumamos 1 a su contador
        if elemento in contador:
            contador[elemento] += 1
        else:
            # Si no está, lo añadimos al diccionario y ponemos 1
            contador[elemento] = 1

    # Creamos una lista vacía donde guardaremos los elementos que salen más de una vez
    duplicados = []

    # Usamos .items() para recorrer el diccionario y obtener tanto la clave como el valor:
    # - clave será el número del array original
    # - valor será la cantidad de veces que aparece ese número
    for clave, valor in contador.items():
        # .items() devuelve tuplas (clave, valor) por cada par guardado en el diccionario.
        # En cada vuelta del bucle, clave y valor toman valores como (4, 2) si el 4 aparece dos veces.

        # Si el valor es mayor que 1, significa que ese número está repetido
        if valor > 1:
            duplicados.append(clave)  # Lo añadimos a la lista de duplicados

    # Finalmente, ordenamos la lista de duplicados de menor a mayor antes de devolverla
    duplicados.sort()
    return duplicados

