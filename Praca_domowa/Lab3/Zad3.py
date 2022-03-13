# Zad3: Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość - jednostka
# w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension do zdefiniowania nowej listy, gdzie
# będą produkty, których wartość to sztuki.

sklep1 = {"papryka": "kg", "jajka": "sztuki", "mąka": "kg", "mleko": "l", "ogórek": "sztuki"}
sklep2 = [i for i in sklep1.keys() if sklep1[i] == "sztuki"]

print(sklep2)
