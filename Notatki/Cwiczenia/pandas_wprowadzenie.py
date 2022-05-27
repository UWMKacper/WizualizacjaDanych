import pandas as pd
import numpy as np

# Zadanie 1. Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx
xlsx = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

# Zadanie 2. Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
df[df['Liczba']>1000]

# tylko rekordy gdzie nadane imię jest takie jak Twoje
df[(df['Imie']=='KACPER')]

# sumę wszystkich urodzonych dzieci w całym danym okresie
a = df.groupby(['Rok']).sum()
# print(a)

# sumę dzieci urodzonych w latach 2000-2005
a = sum(df['Liczba'][(df['Rok']>=2000) & (df['Rok']<=2005)])
# print(a)
# sumę urodzonych chłopców i dziewczynek,
chlopcy = sum(df['Liczba'][(df['Plec']=='M')])
dziewczynki = sum(df['Liczba'][(df['Plec']=='K')])
suma = f"""Liczba chłopców: {chlopcy}
Liczba dziewzcynek: {dziewczynki}
Suma: {chlopcy+dziewczynki}"""

a = df['Liczba'].sum()
# print(a)

# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
imiona = df.groupby(['Rok', 'Plec'])
print(imiona.head(1))

# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
a = df[df['Plec']=='M']
b = a.groupby(['Imie','Plec']).sum(['Liczba'])
c = b.sort_values(by='Liczba')
# print(c.tail(1))

a = df[df['Plec']=='K']
b = a.groupby(['Imie','Plec']).sum(['Liczba'])
c = b.sort_values(by='Liczba')
print(c['Liczba'].max())
print(c.tail(1))

# Zadanie 3
# Wczytaj plik /datasets/zamowieniana.csv
df = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')

# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
kolumna = df.groupby('Sprzedawca')
etykiety = list(kolumna.groups.keys())
#print(etykiety)

# 5 najwyższych wartości zamówień
# print(df.sort_values(by='Utarg', ascending=False).head(5))

# ilość zamówień złożonych przez każdego sprzedawcę
# print(kolumna['Sprzedawca'].count().reset_index(name='ilosc zamowien'))

# sumę zamówień dla każdego kraju
kolumna = df.groupby('Kraj')
# print(kolumna.agg({'Utarg': ['sum']}))

# sumę zamówień dla roku 2005, dla sprzedawców z Polski
a = df[df['Kraj']=='Polska']
b = a[a['Data zamowienia']>='2005-01-01']
c = b[b['Data zamowienia']<='2005-12-31']
# print(c.agg({'Utarg': ['sum']}))

# średnią kwotę zamówienia w 2004 roku
a = df[df['Data zamowienia']>='2004-01-01']
b = a[a['Data zamowienia']<='2004-12-31']
# print(b.agg({'Utarg': ['mean']}))

#zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
kolumna = df.groupby('Kraj')
a = df[df['Kraj']=='Polska']
b = a[a['Data zamowienia']>='2005-01-01']
c = b[b['Data zamowienia']<='2005-12-31']
# c.to_csv('zamówienia_2005.csv', index=False, header=0, sep=';', decimal='.')

a = df[df['Data zamowienia']>='2004-01-01']
b = a[a['Data zamowienia']<='2004-12-31']
# b.to_csv('zamówienia_2004.csv', index=True, header=0, sep=';', decimal='.')