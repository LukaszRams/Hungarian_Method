import numpy as np
import HungarianMethod
from typing import Tuple

#Zwraca minimalną listę wierszy i listę kolumn zawierających wszystkie zera w macierzy = pokrycie wierzchołkowe
def cross_zeros_off(A:np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    
    independent_zero = 1 #Oznaczenie zera niezależnego
    dependent_zero = 2 #Oznaczenie zera zależnego
    
    n = len(A) #Wymiar macierzy
    
    if n != len(A[0]): #Funkcja przyjmuje tylko macierze kwadratowe
        print("Macierz nie jest kwadratowa")
        return 0
    
    #True -> oznaczam wiersz lub kolumne symbolem x
    B1 = np.zeros(n, bool) #Wektor zakreśleń wierszy 
    B2 = np.zeros(n, bool) #Wektor zakreśleń kolumn
    
    new = 1
    while new == 1: #Sprawdzenie czy w poprzedniej pętli dodano nowy element
        new = 0
        
        #-----Oznaczanie symbolem x każdy wiersz nie posiadający zera niezależnego-----
        for i in range(n):
            independent_zero_exist = False
            for j in range(n):
                if A[i][j] == independent_zero:
                    independent_zero_exist = True
            if independent_zero_exist == False:
                if B1[i] == False:
                    new = 1
                B1[i] = True
                

        #-----Oznaczanie symbolem x każdą kolumnę posiadajęcą zero zależne w oznaczonym wierszu-----
        for i in range(n):
            for j in range(n):
                if A[i][j] == dependent_zero and B1[i] == True:
                    if B2[j] == False:
                        new = 1
                    B2[j] = True


        #-----Oznaczanie symbolem x każdy wiersz mający zero niezależne w oznakowanej kolumnie-----
        for i in range(n):
            for j in range(n):
                if A[i][j] == independent_zero and B2[j] == True:
                    if B1[i] == False:
                        new = 1
                    B1[i] = True
    
    #-----Pokrycie wierzchołkowe = wszystkie nieoznakowane wiersze i oznakowane kolumny-----
    row = np.logical_not(B1)
    column = B2
    
    print("Oznaczone wiersze: ", row)
    print("Oznaczone kolumny: ", column)
    
    return row, column
