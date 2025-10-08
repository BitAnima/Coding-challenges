"""Space Week Day 4: Landing Spot
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

Each spot in the matrix will contain a number from 0-9, inclusive.
Any 0 represents a potential landing spot.
Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
Return the indices of the safest landing spot. There will always only be one safest spot.
For instance, given:

[
  [1, 0],
  [2, 0]
]
Return [0, 1], the indices for the 0 in the first array."""

"""
Space Week Day 4: Landing Spot

Este módulo implementa la función find_landing_spot, que calcula la posición
más segura para aterrizar en una matriz representando peligros, según la suma
de los vecinos inmediatos (arriba, abajo, izquierda y derecha) alrededor de
cada celda con valor cero.

Funciones:
    - find_landing_spot(local_map): Identifica la posición [fila, columna] de
      un '0' rodeado por la mínima suma de peligros.

Ejemplo de uso:
    >>> mapa = [
    ...     [1, 0],
    ...     [2, 0]
    ... ]
    >>> find_landing_spot(mapa)
    [0, 1]
"""

from typing import List

def find_landing_spot(local_map: List[List[int]]) -> List[int]:
    """
    Busca la posición [fila, columna] de un '0' rodeado por la suma mínima
    de sus vecinos (sin contar diagonales ni salirse de la matriz).

    Parámetros:
        local_map (List[List[int]]): matriz de enteros (0-9), el mapa de peligros.

    Devuelve:
        List[int]: [fila, columna] del landing spot más seguro.

    Ejemplo:
        >>> find_landing_spot([[1, 0], [2, 0]])
        [0, 1]
    """

    minimum_danger_sum = float('inf')
    best_spot = None

    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)] #(-1, 0) arriba; (1, 0) abajo; (0, -1) izquierda; (0, 1) derecha

    num_rows = len(local_map)
    num_cols = len(local_map[0])

    for fila, valores_fila in enumerate(local_map):
        for columna, valor in enumerate(valores_fila):
            if valor == 0:
                print(f"Cero encontrado en ({fila}, {columna})")

                neighbor_sum = 0
                for desplazamiento_fila, desplazamiento_columna in neighbors:
                    neighbor_row = fila + desplazamiento_fila
                    neighbor_columna = columna + desplazamiento_columna
                    # Solo suma si está dentro de los límites:
                    if 0 <= neighbor_row < num_rows and 0 <= neighbor_columna < num_cols:
                        neighbor_sum += local_map[neighbor_row][neighbor_columna]

                #Buscamos el valor mínimo
                if neighbor_sum < minimum_danger_sum:
                    minimum_danger_sum = neighbor_sum
                    best_spot = [fila, columna]
    return best_spot


