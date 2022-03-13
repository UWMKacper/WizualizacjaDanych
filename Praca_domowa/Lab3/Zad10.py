# Zad10: Z przedziału od 0 do 100 wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

lista = [i for i in range(101) if i % 4 == 0]
filename = "lista.txt"
with open(filename, "w") as f:
    for liczba in lista:
        f.write(str(liczba) + '\n')

    print(f"Został utworzony plik: {filename}")
