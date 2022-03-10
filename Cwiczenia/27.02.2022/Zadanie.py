#
#
# for i in range(1):
#     a = int(input("Wporwadź liczbę a: "))
#     b = int(input("Wporwadź liczbę b: "))
#     c = int(input("Wporwadź liczbę c: "))
#     d = int(input("Wporwadź liczbę d: "))
#
#     if (a > b) & (c > d):
#         print("TAK")
#     else:
#         print("NIE")
#
# for i in range(0,6,1):
#     print(i)
#
# for i in [1,2,2,3]:
#     print(i)
#
# lista = [1,2,3,4,5,6]
# liczba = int(input("Podaj liczbę: "))
# licznik = 0
#
# while licznik != len(lista):
#     if int(liczba) - lista[licznik] == 0:
#         print(f"{liczba} - {lista[licznik]} = 0")
#         break
#     else:
#         licznik += 1
#
# lista1 = [1,2,3,5,6,7,3,5]
# lista2 = [3,6,3,35,2,5,2]
# suma = []
#
# for i in lista1:
#     for k in lista2:
#         suma.append(i+k)
#     print(suma)
import random

# liczba1 = 2
# liczba2 = 0
# try:
#     dziel = liczba1/liczba2
# except ZeroDivisionError as e:
#     print(f"Wystąpił błąd: {e}")
# else:
#     print("Else")
# finally:
#     print("Finally")

lista = []
slownik = {}

print("Aktualny stan:")
print(f"Lista: {lista}")
print(f"Słownik: {slownik}")

print("\nDodawanie elementu do listy i słownika:")
lista.extend(["Klucz",2])
slownik['klucz'] = 'KEY'

print("\nAktualny stan:")
print(f"Lista: {lista}")
print(f"Słownik: {slownik}")

print("\nUsuwanie elementu z listy i słownika:")
lista.pop()
lista.remove(lista[0])
del slownik['klucz']

print("\nAktualny stan:")
print(f"Lista: {lista}")
print(f"Słownik: {slownik}")
