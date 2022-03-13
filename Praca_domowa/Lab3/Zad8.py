# Zad8: Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz to nazwa
# produktu a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową
# wartość tych produktów.

def zakupy(**args):
    print("Liczba wszystkich produktów: ", len(args))
    print("Całkowita wartość produktów: ", sum(args[i] for i in args))


zakupy(marchew=5, olej=10, sok=1.1)
