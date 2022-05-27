import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Zad.1. Odwzoruj wykres znajdujący się w pliku graficznym 1.png znajdującym się folderze. Odcienie kolorów
# mogą się różnić, jednak główne barwy muszą być zachowane. Zapisz powstały wykres w formacie pdf.

# wykres kolumnowy
etykiety = [0, 0, 1, 1, 2, 2, 3, 3, 4, 5]
wartosc = [101, 20, 75, 10, 76, 30, 28, 10, 50, 0]

# kolory jako RGB można podwać w postaci touple: (29/255, 139/255, 125/255)
# plt.bar(x=etykiety, height=wartosc, color=[
#     (29/255, 139/255, 125/255), (98/255, 78/255, 161/255), 'darkgreen', 'deepskyblue', 'darkkhaki', 'olive', 'pink', 'royalblue', 'limegreen', 'white'])
# plt.ylim((0,140)) # zakres dla osi y
# plt.title('Tytuł')
# plt.xlim(right=5.25)
# x1 = np.arange(0, 6 , 1)
# y1 = np.array([120 for i in x1])
#
# plt.plot(x1, y1, '-', color='darkgreen')
#
# plt.show()

# # Zad.2. W jednym pliku wykonaj poniższe czynności:
# # załaduj dane z pliku mieszkania1.xlsx jako ramkę danych (Data Frame)
# xlsx = pd.ExcelFile('mieszkania1.xlsx')
# df = pd.read_excel(xlsx, header=0)
# x_axis = 1
# y_axis = 5
# # stwórz wykres słupkowy pionowy prezentujący dane zawarte w ramce danych (wszystkie dane)
# os_x = df.groupby('Rok').agg('count')
# kolumna = df.groupby('Rok')['Wartość'].agg('sum')
#
# plt.bar(x=os_x.index, height=list(kolumna), color=['red', 'green', 'blue', 'yellow'])
# plt.locator_params(integer=True) # zmienia wartości na osi x na całkowite
# plt.ylim(top=80000)
# plt.xlabel('Lata')
# plt.ylabel('Suma wartości')
# plt.title("Zależność sumy wartości od lat")
#
# # umieść swój numer indeksu w lewym górnym rogu wykresu
# # umieszczenie tekstu w dowolnym miejscu
# plt.text(2014.5, 75000, "nr indeksu", fontsize=12)
# # plt.show()
#
# # Zapisz wykres w formacie pdf za pomocą kodu.
# # Zapisanie wykresów do plików png
# plt.savefig('zadanie2.png')
#
# # konwersja wykresu do pliku pdf
# im1 = Image.open('zadanie2.png')
# im1 = im1.convert('RGB')
# im1.save('zadanie2.pdf')

# Zad.3. W jednym pliku wykonaj poniższe czynności:
xlsx = pd.ExcelFile('turystyka1.xlsx')
df = pd.read_excel(xlsx, header=0)
# uporządkuj dane tak, aby dane liczbowe były zgodne z koncepcją “czystych danych” (w kolumnach)

# zamiana kolumn na wiersze
x = pd.melt(df)
#{kategoria:{rok: {'wartosc': int}
arr = {}

# bruteforce do uporządkowania danych
for key in df.keys():
    if '.' in key:
        key = key[:key.index(".")]
    if key not in arr:
        arr[key] = {}

for key in df.keys():
    value = int(df[key][1])
    year = int(df[key][0])
    if '.' in key:
        key = key[:key.index(".")]
    if year not in arr[key]:
        arr[key][year] = {"value": value}
    else:
        arr[key][year]['value'] += value

kategorie_2014 = []
wartosci_2014 = []
for kat in arr:
    if 2014 in arr[kat]:
        kategorie_2014.append(kat)
        wartosci_2014.append(arr[kat][2014]['value'])

kategorie_2015 = []
wartosci_2015 = []
for kat in arr:
    if 2015 in arr[kat]:
        kategorie_2015.append(kat)
        wartosci_2015.append(arr[kat][2015]['value'])


# stwórz dwa wykresy kołowe prezentujące względny udział różnych kategorii hoteli w danym roku
# (wybierz dowolne dwa lata samodzielnie)

# Tutaj trzeba jeszcze zrobić subplot, dodać opisy dla tego wykresu np title i zapisać go jako jakieśtam rozszerzenie

plt.subplot(1, 2, 1)# liczba wierzsy, kolumn, indeks wykresu
explode = (0.1, 0.2, 0.3, 0.4, 0.5)
plt.title("Pierwszy wykres")
# explode powoduje wyrwanie kawałka z piecharta

wedges, texts, autotext = plt.pie(x=wartosci_2014,labels=kategorie_2014,explode=explode, shadow=True, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))

plt.subplot(1, 2, 2)# liczba wierzsy, kolumn, indeks wykresu
plt.title("Drugi wykres")
wedges, texts, autotext = plt.pie(x=wartosci_2015,labels=kategorie_2015, shadow=True, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))

plt.subplots_adjust(left=0.15, right=0.85) #, top=0.9, bottom=0.1
plt.subplots_adjust(wspace=0.5)
# plt.show()

# Zapisz wykres w formacie jpg za pomocą kodu.
# Zapisanie wykresów do plików png
plt.savefig('zadanie3.png')

# konwersja wykresu do pliku pdf
im1 = Image.open('zadanie3.png')
im1 = im1.convert('RGB')
im1.save('zadanie3.jpg')

