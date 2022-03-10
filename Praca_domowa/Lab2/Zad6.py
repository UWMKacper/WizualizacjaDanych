# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od wyniku wyświetl
# odpowiedni komunikat. Użyj zagnieżdżeń.

a = int(input("Wprowadź wartość liczby całkowitej 'a': "))
b = int(input("Wprowadź wartość liczby całkowitej 'b': "))
c = int(input("Wprowadź wartość liczby całkowitej 'c': "))

if a > b and a > c:
    print("Największą wartość ma liczba 'a'!")
elif b > a and b > c:
    print("Największą wartość ma liczba 'b'!")
elif c > a and c > b:
    print("Największą wartość ma liczba 'c'!")
elif a == b and a > c:
    print("Największą wartość mają liczby 'a' i 'b'!")
elif a == c and a > b:
    print("Największą wartość mają liczby 'a' i 'c'!")
elif b == c and b > a:
    print("Największą wartość mają liczby 'c' i 'b'!")
else:
    print("Liczby 'a', 'b' i 'c' są sobie równe!")
