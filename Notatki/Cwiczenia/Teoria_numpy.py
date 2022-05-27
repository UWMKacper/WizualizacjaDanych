import numpy as np

# utworzenie arraya na podstawie listy
a = np.array([0, 1])

# zmiana typu danych w array podczas jego tworzenia
b = np.arange(1,5,1,dtype='float64')

# zmiana typu danych w już utworzonym array
c = b.astype('int64')

# wyświetlenie kształtu macierzy
c.shape

# utworzenie macierzy na postawie dwóch innych arrayów
d = np.array([np.arange(2), np.arange(2)])

# utworzenie macierzy o okreslonych wymiarach składającej się z samych zer
zera = np.zeros((5,5), dtype='int64')

# utworzenie macierzy o okreslonych wymiarach składającej się z samych jedynek
jedynka = np.ones((3,3), dtype='int64')

# utworzenie pustej macierzy o okreslonych wymiarach (w jej wnętrzu będa znajdować się jakieś losowe bardzo małe liczby)
pusta = np.empty((2,2))

# utworzenie array od start do stop i ze step
a = np.arange(1,5,0.5)

# utworzenie array od start do stop (jak endpoint=True to włącznie, jak endpoint=False to bez niego) i liczba elementów
b = np.linspace(1, 5, 5, endpoint=True)
b = np.linspace(1, 5, 5, endpoint=False)

# tworzy 2 macierze z indeksami poszczególnych elementów macierzy o przekazanych wymiarach.
# Pierwsza to wiersze druga to kolumny
c, d = np.indices((5,5))

# tworzy 2 macierze z elementami grida o podanym zakresie. Pierwsza wiersze, druga kolumny
f,g = np.mgrid[-2:5, -2:5]

# tworzy macierz która ma na przekątnej podane wyrazy, pozostałe elementy to 0
h = np.diag([a for a in range(5)])

# tworzy macierz która ma główną przekątną przesuniętą o 1 wyraz w dół (bo -1), a pozostałe elementy to 0
h = np.diag([a for a in range(5)],-1)

# tworzy array z obiektu iterowalnego
i = np.fromiter(range(5), dtype='int32')

# tworzy array z obiektu bitowego
# 'S2' - ozacza że przekazany obiekt bitowy zostanie podzielony na elementy dwu-znakowe
marcin = b'Marcin'
mar = np.frombuffer(marcin, dtype='S2')

# tworzy array z obiektu iterowalnego
# 'U2' nie wiem co to oznacza
mar_4 = np.fromiter(marcin, dtype='U2')

# cięcie podanego arraya
a = np.arange(10)
s = slice(2,7,2)
s = range(2, 7, 2)
a[2:7:2]

# zmiana kształtu arraya
b = np.arange(25)
mat = b.reshape((5,5))

# cięcie macierzy
mat[1,0:5]
mat[:,0:5]
mat[2:5, 1:3]
mat[2:4, 0:5]
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = a[rows, cols]

