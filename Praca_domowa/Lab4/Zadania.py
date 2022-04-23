import numpy as np

# Zad 1. Za pomoca funkcji arange stwórz tablice numpy składającą się z 15 kolejnych wilekokrotności liczby 3
print("\nZad 1\n")

z_1 = np.arange(0, 45, 3)
print(z_1)

# Zad 2. Stwórz listę składającą się z wartości zmiennnoprzecinkowych a nastepnie zapisz do innej zmiennej jej kopię
# przekonwertowaną na typ int64
print("\nZad 2\n")

z2_1 = np.array([1, 2, 3, 4, 5, 6], dtype='float64')
z2_2 = z2_1.astype('int64')
print(z2_1)
print(z2_2)

# Zad 3. Napisz funkcje, która bedzie przyjmowała jeden parametr 'n' w postaci liczby całkowitej i zwracała tablicę o
# wymiarach n*n kolejnych liczb całkowitych poczynając od 1
print("\nZad 3\n")


def func_z3(n):
    """Func returns matrix in shape n x n."""
    start = 0
    end = n
    body = []
    for _ in range(n):
        body.append(np.arange(start, end))
        start = end
        end = end + n
    return np.array(body)


z_3 = func_z3(5)
print(z_3)

# Zad 4. Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz
# ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg
# podanej liczby, np. generuj(2,4) -> [2,4,8,16]
print("\nZad 4\n")


def func_z4(x, y):
    return list(np.logspace(1, y, num=y, base=x, dtype=int))


print(func_z4(2, 4))

# Zad 5. Napisz funkcję, która:
# Na wejściu przyjmuje jeden parametr określający długość wektora
# Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# Generuj macierz diagonalną z w/w wektorem jako przekątną
print("\nZad 5\n")


def func_z5(x):
    return np.diag(np.arange(x)[::-1])


print(func_z5(5))

# Zad 6. Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie. Jedno z tych słów powinno być
# wypisane od prawej do lewej.
print("\nZad 6\n")

wiersz_1 = "tak"
np_wiersz_1 = np.array(list(wiersz_1))[::-1]
wiersz_2 = "ara"
np_wiersz_2 = np.array(list(wiersz_2))
wiersz_3 = "cuk"
np_wiersz_3 = np.array(list(wiersz_3))
wykreslanka = np.array([np_wiersz_1, np_wiersz_2, np_wiersz_3])
print(wykreslanka)

# Zad 7. Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2
# na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.
print("\nZad 7\n")


def func_z7(n):
    # wyznaczenie macierzy warunkującej czy dane elementy wierszy będą się dodawać bądź odejmować
    direction = [1]
    direction.extend([-1 for _ in range(n - 1)])

    # utworzenie pierwszego wiersza poszukiwanej macierzy
    array = [[2 * i for i in range(1, n + 1)]]

    for i in range(n - 1):
        new_array = [2 * k for k in direction]
        row = np.add(array[i], new_array)
        array.append(row)
        # jeżeli dojdziemy do 2 to teraz należy dodawać, a nie odejmować kolejne liczby
        if 2 in row:
            direction[np.where(row == 2)[0][0]] = 1
    return np.array(array)


print(func_z7(4))

# Zad 8.Napisz funkcję, która:
# jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn,
# w zależności od kierunku podziału, nie pozwala na operację)
print("\nZad 8\n")


def func_z8(array, kierunek):
    wiersze = len(array)
    kolumny = len(array[0])
    if kierunek == "poziom":
        assert wiersze % 2 == 0, 'Liczba wierszy musi być parzysta, aby je podzielic na pol w poziomie'
        return array[0:wiersze // 2, 0:kolumny], array[wiersze // 2:wiersze, 0:kolumny]
    elif kierunek == "pion":
        assert kolumny % 2 == 0, 'Liczba kolumn musi być parzysta, aby je podzielic na pol w pionie'
        return array[0:wiersze, 0:kolumny // 2], array[0:wiersze, kolumny // 2:kolumny]
    else:
        raise "Przekazano niewłaściwą wartość w parametrze 'kierunek'."


b = np.arange(16)
mat = b.reshape((4, 4))

x, y = func_z8(mat, "poziom")
print(x)
print(y)
a, b = func_z8(mat, "pion")
print(a)
print(b)

# Zad 9. Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała
# kolejne wartości ciągu Fibonacciego.
print("\nZad 9\n")

# wyznaczenie pierwszych 25 elementow ciagu Fibonacciego
fib_arr = [0, 1]
for i in range(1, 24):
    fib_arr.append(sum(fib_arr[-2:]))

# utworzenie macierzy 5x5
nearly_fibb = np.array(fib_arr)
fibb = nearly_fibb.reshape((5, 5))

print(fibb)
