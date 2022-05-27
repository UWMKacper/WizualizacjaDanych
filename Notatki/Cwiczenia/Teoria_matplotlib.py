import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import  Image

# # wyświetlenie wykresu wektora [1, 2, 3, 4]
# plt.plot([1, 2, 3, 4])
# plt.ylabel('liczby z wektora')
# plt.show()
#
# # wyświetlenie wykresu wektorów: [1, 2, 3, 4], [1, 4, 9, 16] pierwszy odpowada za x, drugi za y
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro:') # r- kolor czerowny, o- oznaczone puntky na wykresie, :- linia kropkowa
# plt.ylabel('liczby z wektora')
# plt.show()
#
# # wyświetlenie 2 wykresów, czerowny to kropkowy, a niebieski to tylko punkty:
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
# plt.axis([0, 6, 0, 20]) # pierwsze 2 elementy to minimum i maksimum dla osi x, kolejne dwa to minimum i maksimum dla osi y
# plt.show()
#
# wyświetlenie 2 wykresów
# x = np.arange(0, 5.2, 0.2)
# plt.plot(x, x, 'r-', x, x**2, 'b^') # zdefiniowane dwa wektory w jednej linijce: wartości x, wartości y, styl wykresu
# plt.show()
#
# # wyświetlenie 3 wykresów
# x = np.arange(0, 5.2, 0.2)
# plt.plot(x, x, 'r-', x, x**2, 'b^',x , x**3, 'gs')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'], loc='center left') # labels: dodawanie legendy do wykresu, loc: lokalizacja legendy
# plt.show()
#
# # Zapisanie wykresów do plików png
# plt.plot(x, x, label='liniowa')
# plt.plot(x, x**2, label='kwadratowa')
# plt.plot(x, x**3, label='sześcienna')
# plt.legend()
# plt.savefig('plot.png')
#
# # konwersja wykresu do pliku jpg
# im1 = Image.open('plot.png')
# im1 = im1.convert('RGB')
# im1.save('plot.jpg')
# plt.show()

# # Zad z cwiczeń - utworzyć 2 wykresy na podstawie podanych x i y
# # dane do wsadu
# x_1 = np.array([i for i in range(1, 21)])
# y_1 = np.array([1/i for i in x_1])
# x_2 = np.arange(0, 10, 0.1)
# y_2 = np.array(np.sin(x_2))
# #
# # pierwszy wykres
# plt.plot(x_1, y_1, 'g-', label='wykres 1')
# plt.legend()
# plt.show()
#
# # drugi wykres
# plt.plot(x_2, y_2, 'b^', label='wykres 2')
# plt.legend()
# plt.show()

# grid
# rysowanie siatki - łączenie dwóch wykresów za pomocą np.: subplot
# x1 = np.arange(0, 2.02, 0.02)
# x2 = np.arange(0, 2.02, 0.02)
# y1 = np.sin(2*np.pi*x1)
# y2 = np.cos(2*np.pi*x2)
# #
# # pierwszy wykres
# plt.subplot(2, 1, 1)# liczba wierzsy, kolumn, indeks wykresu
# plt.plot(x1, y1, 'r--')
# plt.ylabel('sin(y)') # etykieta do osi y
# plt.xlabel('x') # etykieta osi x
# plt.title('wykres sin(x)') # tytuł wykresu
# #
# # # drugi wykres
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'co')
# plt.xlabel('x') # etykieta osi x
# plt.ylabel('cos(y)')
# plt.title('wykres cos(x)') # tytuł wykresu
# plt.subplots_adjust(hspace=0.5) # zwieksza odległość między wykresami
# plt.show()

# # rysowanie siatki - łączenie dwóch wykresów za pomocą np.subplots
# x1 = np.arange(0, 2.02, 0.02)
# x2 = np.arange(0, 2.02, 0.02)
# y1 = np.sin(2*np.pi*x1)
# y2 = np.cos(2*np.pi*x2)
#
# fig, axs = plt.subplots(3, 2) # utworzenie 6 wykresów - 3 wiersze, 2 kolumny
# print(type(fig))
# print(type(axs))
#
# axs[0, 0].plot(x1, y1, 'r-')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('wykres sin(x)')
#
# axs[1, 1].plot(x2, y2, 'g-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('wykres cos(x)')
#
# axs[2, 0].plot(x2, y2, 'g-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# axs[2, 0].set_title('wykres cos(x)')
#
# # usuwanie zbędnych wykresów
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()

# wykres punktowy wielokolorowy
# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# dane['b'] = dane['a'] + 10 * np.random.randn(50)
# dane['d'] = np.abs(dane['d']) * 100
#
# plt.scatter(data=dane, x='a', y='b', c='c', s='d', cmap='plasma') # x - wartości dla x,y - wartości dla y, c - kolor dla każdego punktu, s - rozmiar dla każdego punktu, cmap - paleta kolorów
# plt.xlabel('wartosci a')
# plt.ylabel('wartosci b')
# plt.show()
#
# # wykres punktowy jednokolorowy
# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# dane['b'] = dane['a'] + 10 * np.random.randn(50)
# dane['d'] = np.abs(dane['d']) * 100
#
# plt.scatter(data=dane, x='a', y='b', color='orange', s='d') # color - dla jednego koloru
# plt.xlabel('wartosci a')
# plt.ylabel('wartosci b')
# plt.show()

# wykres kolumnowy
data={'Kraj':['Belgia','Indie','Brazylia', 'Polska'],
      'Staolica':['Bruksela', 'New Delhi','Brasilia', 'Wadowice'],
      'Populacja':[2137,1132,2222, 666],
      'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}

df = pd.DataFrame(data)
print(df)
grupa = df.groupby('Kontynent')
etykiety = list(grupa.groups.keys())
wartosc = list(grupa.agg('Populacja').sum())

# wykres pionowy
plt.bar(x=etykiety, height=wartosc, color=['red', 'green', 'blue'])
# wykres poziomy
# plt.barh(y=etykiety, width=wartosc, color=['red', 'green', 'blue'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja na kontynentach')
plt.show()

# histogram
# x = np.random.randn(10000)
# plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True) # wektor, bins-liczba słupków, facecolor-kolor słupków, alpha-przeźroczystość, density=idk dawaj zawsze True
# plt.xlabel('wartosci x')
# plt.ylabel('prawodpodobienstwa')
# plt.show()