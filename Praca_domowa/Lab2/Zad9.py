# Zad. 9. Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość
# ujemną to powinien być wyłapany błąd.
import math
try:
    liczba = float(input("Podaj liczbę: "))

    print(f"Pierwiastek z {liczba} wynosi: {math.sqrt(liczba)}")
except ValueError as e:
    print(f"Wystąpił błąd: {e}")
