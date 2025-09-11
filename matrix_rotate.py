"""Matrix Rotate
Given a matrix (an array of arrays), rotate the matrix 90 degrees clockwise and return it. For instance, given [[1, 2], [3, 4]], which looks like this:

1	2
3	4
You should return [[3, 1], [4, 2]], which looks like this:

3	1
4	2


Tests
Waiting:1. rotate([[1]]) should return [[1]].
Waiting:2. rotate([[1, 2], [3, 4]]) should return [[3, 1], [4, 2]].
Waiting:3. rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [[7, 4, 1], [8, 5, 2], [9, 6, 3]].
Waiting:4. rotate([[0, 1, 0], [1, 0, 1], [0, 0, 0]]) should return [[0, 1, 0], [0, 0, 1], [0, 1, 0]]."""

def print_matrix(matrix, mensaje):
    print(mensaje)
    for fila in matrix:
        print('\t'.join(str(x) for x in fila))
    print()

def rotate(matrix):
    # Imprime la matriz original
    print_matrix(matrix, "Matriz original:")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"Elemento en fila {i}, columna {j}: {matrix[i][j]}")
    
    print("\nRotando la matriz 90 grados en el sentido de las agujas del reloj...\n")
    n = len(matrix)

    # Paso 2: Transponer la matriz
    # Intercambia matrix[i][j] con matrix[j][i] para convertir filas en columnas
    # Ejemplo: [[1, 2], [3, 4]] -> [[1, 3], [2, 4]]
    for i in range(n):
        for j in range(i, n):
            print(f"Intercambiando ({i},{j})={matrix[i][j]} con ({j},{i})={matrix[j][i]}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print_matrix(matrix, f"Matriz después de intercambiar ({i},{j}) y ({j},{i}):")

    # Paso 3: Invertir cada fila
    # La función .reverse() invierte el orden de los elementos de la lista en el lugar.
    # Esto convierte la matriz transpuesta en la matriz rotada 90 grados.
    # Ejemplo: [[1, 3], [2, 4]] -> [[3, 1], [4, 2]]
    for i in range(n):
        print(f"Invirtiendo fila {i}: antes {matrix[i]}", end=" ")
        matrix[i].reverse()
        print(f"después {matrix[i]}")

    print_matrix(matrix, "Matriz rotada 90° en sentido horario:")
    return matrix

matrix = [[1, 2], [3, 4]]
rotate(matrix)