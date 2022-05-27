import pandas as pd
import numpy as np

# Zadanie 1. Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.
macierz_1_1 = np.array([[1], [2], [3]])
macierz_1_2 = np.array([[4], [5], [6]])
# wynik obliczeń
# print(macierz_1_1*macierz_1_2)

# Zadanie 2. Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.
macierz_2_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

min_wiersze = np.amin(macierz_2_1, axis=0)
min_kolumny = np.amin(macierz_2_1, axis=1)
# print('Min dla każdego wiersza: ', min_wiersze)
# print('Min dla każdej kolumny: ', min_kolumny)

# Zadanie 3. Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.

# wynik obliczeń
# macierz_1_1.dot(macierz_1_2)                          # tu jest jakiś błąd

# Zadanie 4. Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite,
# a druga liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

macierz_4_1 = np.array([[1], [2], [3]])
macierz_4_2 = np.array([[4.5], [5.5], [6.5]])

# wyynik obliczen
# print(macierz_4_1*macierz_4_2)

# Zadanie 5. Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z
# jej wartości i zapisz do zmiennej “a”.

macierz_5_1 = np.array([[1, 2, 3], [4, 5, 6]])

# wynik obliczeń
a = np.sin(macierz_5_1)

# Zadanie 6. Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości
# i zapisz do zmiennej “b”.

macierz_6_1 = np.array([[1, 2, 3], [4, 5, 6]])

# wynik obliczeń
b = np.cos(macierz_6_1)

# Zadanie 7. Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

# wynik obliczeń
a + b

# Zadanie 8. Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
macierz_8_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# wynik obliczeń
for row in macierz_8_1:
    # print(row)
    pass

# Zadanie 9. Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji
# “spłaszczenia” macierzy. (użyj funkcji flat())
macierz_8_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
macierz_8_1 = macierz_8_1.flat

# wynik obliczeń
for el in macierz_8_1:
    # print(el)
    pass

# Zadanie 10. Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
macierz_10_1 = np.array([i for i in range(81)])
macierz_10_2 = macierz_10_1.reshape([9,9])

# wynik obliczeń
macierz_10_3 = macierz_10_2.reshape([81, 1])
"Możemy zrobić reshape macierzy na taki który będzie miał tyle samo elementów co macierz z której robimy" \
"reshape."

# Zadanie 11. Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

macierz_11_1 = np.array([i for i in range(12)])
macierz_11_2 = macierz_11_1.reshape([4, 3])
macierz_11_3 = macierz_11_1.reshape([2, 6])

macierz_11_1 = macierz_11_1.flat
macierz_11_2 = macierz_11_2.flat
macierz_11_3 = macierz_11_3.flat

# wynik końcowy
print(macierz_11_1)
print(macierz_11_2)
print(macierz_11_3)

print(macierz_11_1 == macierz_11_2)
print(macierz_11_2 == macierz_11_3)
print(macierz_11_1 == macierz_11_3)

"""Same obiekty są różne i znajdują się w różnych miejscach w pamięci, lecz wartości elementów
znajdujących się w poszczególnych obiektach w tych samych wierszach i kolumnach będą równe."""