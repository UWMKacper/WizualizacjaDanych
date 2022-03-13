# Zad4: Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

def czy_trojkat_jest_prostokatny(a, b, c):
    boki = sorted([a, b, c])
    return boki[0] ** 2 + boki[1] ** 2 == boki[2] ** 2


# przykład 1
a = 3
b = 4
c = 5

test = czy_trojkat_jest_prostokatny(a, b, c)
print(f"Trójkąt o bokach a = {a}, b = {b}, c = {c} {'' if test else 'nie'} jest trójkątem prostokątnym.")

# przykład 1
a = 6
b = 4
c = 3

test = czy_trojkat_jest_prostokatny(a, b, c)
print(f"Trójkąt o bokach a = {a}, b = {b}, c = {c} {'' if test else 'nie'} jest trójkątem prostokątnym.")
