import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# sumowanie wyrazów macierzy: wszystkich, po kolumnach, po wierszach
basic = np.array([i for i in range(12)])
basic_nice = basic.reshape((4, 3))

basic_nice.sum() # suma wyrazów wszystkich elementów macierzy
basic_nice.sum(axis=0) # suma wyrazów dla każdej kolumny oddzielnie
basic_nice.sum(axis=1) # suma wyrazów dla każdego wiersza oddzielnie

# mnożenie macierzy
a = np.array([[2, 5, 1], [5, 7, 1]])
b = np.array([[2, 3], [4, 5], [7, 1]])
c = np.dot(a, b)

d = a.dot(b) # inny sposób na przemnożenie macierzy a i b

# iloczyn skalarny dwóch wektorów
e = np.arange(3)
f = np.arange(3)

np.dot(e, f)

# wylistowanie po kolei każdego elementu wiersza z podanej macierzy
a = np.arange(6).reshape((3, 2))
for i in a.flat:
    i

# spłaszczenie macierzy do jednego wiersza z większą liczbą kolumn
c = a.reshape((2, 3))
b = c.ravel()

# transpozycja macierzy
d = c.T

# data series
# seria danych - wyświetlanie danych z domyślnymi etykietami indeksów
s = pd.Series([1, 3, 4, 'a', 3.5])

# seria danych - wyświetlanie danych z określonymi etykietami indeksów
s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd'])

# data frame
# ramka danych - wyświetlanie jak tabela z domyslmymi etykietami indeksów
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [2312434124, 2134234234234, 123123123445]
        }
df = pd.DataFrame(data)

# ramka danych - wyświetlanie jak tabela z określonymi etykietami indeksów i określonymi kolumnami
daty = pd.date_range('20220507', periods=5)
df2 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))

# CSV
# wczytanie danych z pliku csv:
#   header = numer wiersza który jest nagłówkiem
#   sep = znak rozdzielający kolumny
#   decimal = znak rozdzielający wartości dziesiętne
df3 = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')

# zapis danych do pliku csv:
#   index = jak True to kolumna z indeksami jest zapisywana
df3.to_csv('dane2.csv', index=False)
df3.to_csv('dane3.csv', index=True)

# excel/xlsx/xlx
# załadowanie danych z excela
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# zapis danych do excela
df.to_excel('imiona2.xlsx', sheet_name='dane')

import openpyxl
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [2312434124, 2134234234234, 123123123445]
        }
df = pd.DataFrame(data)

# df.iloc wyświetla okreslony wiersz
df.iloc[[0]]

# wyświetlanie określonego elementu
df.iloc[[0], [0]]# jak się poda też parametr kolumny to może wyświetlić określony element
df.loc[[0], ['Kraj']]
df.at[0, 'Kraj'] # tu się podaje wierz, nazwa kolumny

# wyświetl (x) x losowych wierszy z danego df
df.sample(2)
df.sample(2, replace=True) # gdy replace=True to wiersze będą mogły się powtarzać

# suma dla każdego wiersza
f=np.arange(12).reshape((3,4))
f.sum(axis=1)

# utworzenie dataframe na podstawie dat
daty=pd.date_range('20221201', periods=5)
df2=pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))

# pierwsze 10 wierszy
df3=pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
xlsx=pd.ExcelFile('imiona.xlsx')
df4=pd.read_excel(xlsx, header=0)
df3.to_csv('dane2.csv',index=False)
df4.to_excel('imiona2.xlsx', sheet_name='dane')
df4.head(10)

# ostatnie 10 wierszy
df4.tail(10)

# wyświetlenie wierszy spełniających określone warunki dla serii
s = pd.Series([10, 12, 14, 8], index=['a', 'b', 'c', 'd'])
s[s>8]
s[(s<13) & (s>8)]
s.where(s>10)
s.where((s>10), 'warunek niespelniony') # dla wierszy które nie spełniły warunku wyświetlone jest 'NaN'
seria = s.copy()
seria.where(s>10, 'warunek niespelniony', inplace=True) # dla wierszy które nie spełniły warunku wyświetlony jest przekazany do funkcji tekst

# wyświetlenie wierszy spełniających określone warunki dla data frame
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [2312434124, 2134234234234, 123123123445]
        }
df = pd.DataFrame(data)
df['Populacja']
df[df['Populacja'] > 1200]

# wstawianie nowego wiersza na określonej pozycji w data frame
df.loc[3] = 'nowy element'
df.loc[4] = ['Polska', 'Warszawa', 9999]

# usuwanie określonego wiersza w data frame
df.drop([3], inplace=True)

# dodanie nowej kolumny w dataframe
df['Kontynent'] = ['Europa', 'Azja', 'Aneryka Poludiowa', 'Europa']

# sortowanie po kolumnach w dataframe
df.sort_values(by='Kraj')
df.sort_values(by='Kraj', ascending=False)

grupa = df.groupby(by='Kontynent').agg({'Populacja': ['sum']})

# te funkcje nie działają i nie wiem czemu
# print(grupa.get_group('Europa'))
# print(grupa.agg({'Populacja': ['sum']}))



# matplotlib
# rysowanie wykresów słupkowych
grupa.plot(kind='bar', xlabel='Kontynenty', ylabel='Populacja', rot=0, title='Populacja na kontynentach')

# zapis wykresu do pliku
plt.savefig('plot1.png')

# inny sposób rysowania wykresów
wykres = grupa.plot.bar()
wykres.set_xlabel('Kontynent')
wykres.set_ylabel('Populacja w mld')
wykres.tick_params(axis='x', labelrotation=0)
wykres.set_title('Populacja na kontynentach')

# wyświetlenie wszystkich utworzonych wykresów
plt.show()

# rysowanie wykresu kołowego
grupa = df3.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, colors=['red', 'green'],
           figsize=[15, 15])
plt.legend(loc='upper left')
plt.show()

# rysowanie wykresów punktowych
seria = pd.Series(np.random.randn(1000))
seria = seria.cumsum()
seria.plot()
plt.show()
