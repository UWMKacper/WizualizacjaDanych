# Zad6: Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile
# elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10

def ciag_geometryczny(a=1, b=4, ile=10):
    iloczyn_ciagow = 1
    for i in range(1, ile + 1):
        iloczyn_ciagow *= (a * (b ** (i - 1)))
    return iloczyn_ciagow


print("Iloczyn elementów ciągu wynosi: ", ciag_geometryczny())
