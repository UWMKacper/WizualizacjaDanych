# Zad11: Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli

filename = "lista.txt"

print(f"Zawartość pliku: {filename}:")

with open(filename, "r") as f:
    for i in f.readlines():
        print(i.replace("\n", ""))
