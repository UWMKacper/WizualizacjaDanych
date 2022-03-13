# Zad5: Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.

def pole_trapezu(a=2, b=2, h=2):
    return (a + b) * h * 0.5

print("Dla wartości domyślnych pole trapezu wynosi: ", pole_trapezu())
print("Dla wartości domyślnych pole trapezu dla a=1, b=2, h=3 wynosi: ",pole_trapezu(1, 2, 3))
