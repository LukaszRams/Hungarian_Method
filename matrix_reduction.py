import numpy as np
from typing import Tuple, Optional

def reduce_matrix(matrix: np.ndarray) -> Optional[Tuple[np.ndarray, int]]:

    """
    Funkcja realizuje redukcję macierzy kwadratowej.
    W każdym wierszu wyszukiwany jest element najmniejszy, który następnie jest dodawany do kosztu redukcji oraz
    odejmowany (redukowany) od wszystkich elementów w wierszu.
    Analogiczne działanie dla kolumn macierzy.

    :param matrix: macierz wejściowa
    :return: zredukowana macierz, koszt redukcji
    """

    # Sprawdzenie czy macierz jest kwadratowa:
    if matrix.shape[0] != matrix.shape[1]:
        print('Niepoprawne wymiary macierzy wejściowej')
        return None

    reduction_cost: int = 0  # Koszt redukcji
    reduced_rows_matrix: np.ndarray = np.zeros(matrix.shape)  # Macierz z zredukowanymi wierszami
    reduced_matrix: np.ndarray = np.zeros(matrix.shape)  # Zredukowana macierz

    # Redukcja wierszy
    for i in range(matrix.shape[0]):
        minimum = matrix[i].min()
        reduction_cost += minimum
        row_reduced = [x - minimum for x in matrix[i]]
        reduced_rows_matrix[i] = row_reduced

    print(f'Macierz ze zredukowanymi wierszami:\n {reduced_rows_matrix}')
    print(f'Koszt redukcji wierszy: {reduction_cost}')

    # Redukcja kolumn
    for i in range(matrix.shape[0]):
        minimum = reduced_rows_matrix[:, i].min()
        reduction_cost += minimum
        col_reduced = [x - minimum for x in reduced_rows_matrix[:, i]]
        reduced_matrix[:, i] = col_reduced

    print(f'Zredukowana macierz:\n {reduced_matrix}')
    print(f'Całkowity koszt redukcji macierzy: {reduction_cost}')

    return reduced_matrix, reduction_cost

