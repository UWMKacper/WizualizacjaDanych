# Zad7: Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.

def ciag_geometryczny(*liczby):
    if liczby:
        a = liczby[0]
        b = liczby[1]
        ile = liczby[2]
    else:
        a = 1
        b = 4
        ile = 10

    iloczyn_ciagow = 1
    for i in range(1, ile + 1):
        iloczyn_ciagow *= (a * (b ** (i - 1)))
    return iloczyn_ciagow


print("Iloczyn elementów ciągu wynosi: ", ciag_geometryczny(1, 4, 10))
