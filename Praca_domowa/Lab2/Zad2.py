# Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych. Jako klucz przyjmij
# skrót danego słowa, wartość to rozwinięcie tego skrótu.

# pusty słownik skrótów
skroty = {}

# dodawanie par klucz - wartość do słownika
skroty['al.'] = 'aleja'
skroty['cd.'] = 'ciąg dalszy'
skroty['dr'] = 'doktor'
skroty['itd.'] = 'i tak dalej'
skroty['itp.'] = 'i tym podobne'

# wyświetlenie wszystkich danych ze słownika
print("Zawartość slownika 'skroty':")
for key in skroty.keys():
    print(f"{key} - {skroty[key]}")
