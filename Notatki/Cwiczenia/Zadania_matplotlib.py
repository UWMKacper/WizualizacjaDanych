import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie 1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’)
# oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

# x1 = np.arange(1, 21 , 1)
# y1 = np.array([1/i for i in x1])
#
# plt.plot(x1, y1, 'r--')
# plt.ylabel('f(x)') # etykieta do osi y
# plt.xlabel('x') # etykieta osi x
# plt.ylim((0,1)) # zakres dla osi y
# plt.xlim((1, len(x1))) # zakres dla osi y
# plt.title('wykres sin(x)') # tytuł wykresu
#
# plt.show()

# Zadanie 2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

# x1 = np.arange(1, 21 , 1)
# y1 = np.array([1/i for i in x1])
#
#
# plt.plot(x1, y1, 'g:>', label='f(x) = 1/x')
# plt.ylabel('f(x)') # etykieta do osi y
# plt.xlabel('x') # etykieta osi x
# plt.axis([1, len(x1), 0, 1]) #xx, yy
# plt.title('Wykres funkcji f(x) dla x [1, 20]') # tytuł wykresu
# # plt.plot(x1, y1, 'g^')
# plt.legend()
#
#
# plt.show()

# Zadanie 3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1. Dodaj
# etykiety i legendę do wykresu.

# x1 = np.arange(0, 31, 0.1)
# x2 = np.arange(0, 31, 0.1)
# y1 = np.sin(x1)
# y2 = np.cos(x2)
# #
# # pierwszy wykres
# plt.plot(x1, y1, 'r--', label='sin(x)')
#
# # drugi wykres
# plt.plot(x2, y2, 'g:', label='cos(x)')
#
# # opis
# plt.xlabel('x') # etykieta osi x
# plt.ylabel('y')
# plt.title('wykresy cos(x) i sin(x)') # tytuł wykresu
# plt.legend()
# plt.show()

# Zadanie 5
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# xlsx = pd.ExcelFile('datasets/imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# # Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów
# # stosowne etykiety. Poustawiaj różne kolory dla wykresów.
#
# fig, axs = plt.subplots(1, 3) # utworzenie 6 wykresów - 3 wiersze, 2 kolumny
#
# # 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym
# # okresie.
#
# x1 = 'Urodzenia'
# y1 = df['Liczba'].sum()
# axs[0].bar(x=x1, height=y1, color='red')
# axs[0].set_xlabel('x')
# axs[0].set_ylabel('Liczba urodzeń')
# axs[0].set_title('Suma urodzeń')
#
# # 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla
# # mężczyzn dla każdego roku z osobna. Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x
# # to rok.
#
# # przefiltrowanie podstawgo dataframe, aby zwracał wyniki tylko dla odpowiedniej płci
# kkk = df[df['Plec']=='K']
# mmm = df[df['Plec']=='M']
#
# # pogrópowanie wyników po kolumnie 'Rok' i zwrócenie maksymalnej wartości z kolumny 'Liczba' dla danego roku
# kobiety = kkk.loc[kkk.groupby("Rok")["Liczba"].idxmax()]
# mezczyzni = mmm.loc[mmm.groupby("Rok")["Liczba"].idxmax()]
#
# axs[1].plot(list(kobiety['Rok']), list(kobiety['Liczba']), 'g-')
# axs[1].plot(list(mezczyzni['Rok']), list(mezczyzni['Liczba']), 'b:')
# axs[1].set_xlabel('x')
# axs[1].set_ylabel('cos(x)')
# axs[1].set_title('wykres cos(x)')
#
# # 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.
#
# # Grupowanie po kolumnie 'Rok' i sumowanie z kolumny 'Liczba'
# urodzenia = df.groupby(['Rok'])['Liczba'].agg('sum')
#
# axs[2].bar(x=list(kobiety['Rok']), height=list(urodzenia), color='red')
# axs[2].set_xlabel('Lata')
# axs[2].set_ylabel('Liczba urodzeń')
# axs[2].set_title('Suma urodzeń dla danego roku')
#
# plt.subplots_adjust(wspace=1)

# plt.show()

# Zadanie 6
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego sprzedawcy i wyświetl wykres
# kołowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień. Poszukaj w Internecie jak
# dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego wykresu. Przetestuj ten atrybut na
# wykresie.

df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
kolumna = df.groupby('Sprzedawca')['Utarg'].agg('sum')
# kolumna.index daje indexy wierszy czyli w tym wypadku nazwy sprzdawców
utarg_sprzedwcow = list(kolumna)
df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")

seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()

# explode powoduje wyrwanie kawałka z piecharta
explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)
wedges, texts, autotext = plt.pie(x=utarg_sprzedwcow, shadow=True, explode=explode, labels=kolumna.index, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()