import numpy as np
from typing import Union, Tuple
from collections import Counter
from itertools import product


def set_zeros(matrix: np.ndarray, fi: Union[int, float]) -> Tuple[np.ndarray, np.ndarray, Union[int, float]]:
    """
    ================================================================================================
    Slajd 2
    Poszykiwanie kompletnego przydziału
    ================================================================================================
    
    Funkcja wyznacza zera niezależne oraz zera zależne.
    Zasada działania:

    1. Stworzenie listy list zawierającej informacje o pozycjach zer w każdym wierszu macierzy matrix
    (jeśli zera nie ma w danym wierszu lista zawiera -1) oraz zmiennej best_sol i best_sol_size odpowiednio
    przechowującej informacje o najlepszym rozwiązaniu i liczbie zer przez nie wyznaczonej

    2. Wyznaczenie kombinacji tych pozycji zer
        przykład:
            wejście [[1, 2, 3], [-1], [0, 2]]
            wyjście [(1, -1, 0), (1, -1, 2), (2, -1, 0), (2, -1, 2), (3, -1, 0), (3, -1, 2)]

    3. Wyznaczenie najlepszego dopasowania:
            1. Przejście po wszystkich elementach:
                jeśli wartości w elemencie się powtarzają (z wyjątkiem -1):
                    wybierz następny element
                jeśli nie:
                        jeśli liczba niezależnych zer z danego elementu > best_sol_size:
                            ustaw best_sol_size jako liczba niezależnych zer z danego elementu (tj. rozmiar elementu - liczba wartości "-1")
                            ustaw best_sol jako ten element
                        jeśli nie:
                            wybierz następny element
                jeśli best_sol_size wynosi tyle co rozmiar macierzy:
                    zakończ
                jeśli nie:
                    sprawdź kolejny element

    4. Utwórz macierz z zerami zależnymi i niezależnymi an podstawie best_sol
                    0 - wartość różna od zera w macierzy matrix
                    1 - zero niezależne w macierzy matrix
                    2 - zero zależne w macierzy matrix

    5. Jeśli best_sol_size wynosi tyle co rozmiar macierzy matrix:
            zwróć informacje o przydziale, koszt i zakończ algorytm
       Jeśli nie:
            wywołaj kolejny etap

    :param matrix: przekształcona macierz z etapu I
    :param fi: aktualny koszt
    :return: informacja o przydziale i koszt lub macierz z I etapu, macierz z zerami nie~/zależnymi, aktualny koszt
    """
    # etap 1
    lol: List[List[int]] = list()
    best_sol: Optional[Tuple[int]] = None
    best_sol_size: Optional[int] = None
    size: int = matrix.shape[0]
    for row in matrix:
        lol.append([])
        for col in range(size):
            if row[col] == 0:
                lol[-1].append(col)
        if not len(lol[-1]):
            lol[-1].append(-1)

    # etap 2
    pred_sol: List[Tuple[int]] = list(product(*lol))

    # etap 3
    for elem in pred_sol:
        tmp = Counter(elem)
        tmp2 = False
        for i in range(size):
            if tmp[i] and tmp[i] > 1:
                tmp2 = True
                break
        if tmp2:
            continue
        else:
            if (tmp[-1] and size - tmp[-1] > best_sol_size) or not tmp[-1]:
                best_sol_size = size - tmp[-1] if tmp[-1] else size
                best_sol = elem
            else:
                continue
        if best_sol_size == size:
            break

    # etap 4
    matrix_to_return: np.ndarray = np.zeros((size, size))
    for i in range(size):
        if lol[i][0] != -1:
            for el in lol[i]:
                matrix_to_return[i][el] = 2
    for i in range(size):
        if best_sol[i] != -1:
            matrix_to_return[i][best_sol[i]] = 1

    # etap 5
    if best_sol_size == size:
        fit: str = ""
        for i in range(size):
            fit += f"zadanie: {i} --> maszyna: {best_sol[i]}\n"
        print(matrix)
        print("\nMacierz zer niezależnych")
        print(matrix_to_return)
        print("Dopasowanie:\n", fit, "\nKoszt:\n", str(fi))

    else:
        print(matrix)
        print("\nMacierz zer niezależnych")
        print(matrix_to_return)
        return matrix, matrix_to_return, fi  # tu powinno być wywołanie kolejnej funkcji
