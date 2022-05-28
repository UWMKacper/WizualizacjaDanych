import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# do czyszzcenia danych
# transpozycja potem drop na pierwszą kolumnę i dodać df.columns( z nazwami kolumn)

# df = pd.read_excel('', header=None)
# dfT = df.transpose()
# dfT.columns = ['kategoria hotelu', 'rok', 'ilosc']

# # 1. Stwórz program, a w nim wykonaj czynności za pomocą biblioteki Pandas:
# # Załaduj ramkę danych na podstawie pliku automobile.csv
# df = pd.read_csv('automobile.csv', sep=';', decimal='.')
#
# # Stwórz nową ramkę danych składającą się z wierszy, dla których w kolumnie „Price”
# # wartość jest większa bądź równa 10000.
# df1 = df[df['Price']>=1000]
#
# # Na nowej ramce danych utwórz grupę zliczającą ilość samochodów danej marki.
# df2 = df1.groupby('Car model')['Car model'].agg('count')
#
# # Przedstaw wyniki z poprzedniego podpunktu na wykresie kołowym, dodaj tytuł
# # wykresu, oraz wyświetl wartości procentowe zaokrąglone do dwóch miejsc po
# # przecinku
#
# etykiety = list(df2.keys())
# wartosci = list(df2)
#
# wedges, texts, autotext = plt.pie(x=wartosci, labels=etykiety,
#                                   autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'))
# plt.title("Procentowy udział kwot zamówień sprzedawców")
# # plt.show()
# plt.savefig("Zad 1.png")
# plt.show()

# 2. Za pomocą biblioteki matplotlib odwzoruj wykres dostępny w pliku zad2b.png
data_x = np.arange(-2,4,0.15)
data_y = [-4*(x**2)+(6*x/2)+20 for x in data_x]

plt.plot(data_x, data_y, 'ro')

plt.xticks([-2, -1, 0, -1, 2, 3, 4])
plt.yticks([-25, 0, 25])
plt.grid()
plt.xlim(-2,4)

plt.show()