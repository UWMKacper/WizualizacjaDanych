# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.

lista = []
counter = 1

while counter<11:
    liczba = int(input(f"Podaj liczbę nr {counter}: "))
    if liczba%2 == 0:
        lista.append(liczba)

    counter += 1

print("Lista liczb parzystych: ", lista)