# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
# Użyj instrukcji readline() i write()).

import sys

sys.stdout.writelines("Podaj liczbę a: ")
a = int(sys.stdin.readline())
sys.stdout.writelines("Podaj liczbę b: ")
b = int(sys.stdin.readline())
sys.stdout.writelines("Podaj liczbę c: ")
c = int(sys.stdin.readline())

print(f"ab + c = {a*b + c}")
