# Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj
# mniej lubiane sporty na sam koniec.

lista_sportow = []

dobra_liczba = int(input("Podaj liczbę sportów, które lubisz: "))

for i in range(dobra_liczba):
    sport = input(f"Podaj nazwę {i+1} sportu: ")
    lista_sportow.append(sport)

# odwrócenie kolejności elementów w liście
lista_sportow.reverse()

zla_liczba = int(input("Podaj liczbę sportów, które nie lubisz: "))

for i in range(zla_liczba):
    sport = input(f"Podaj nazwę {i+1} sportu: ")
    lista_sportow.append(sport)

print("Ostateczna postać listy: ", lista_sportow)
