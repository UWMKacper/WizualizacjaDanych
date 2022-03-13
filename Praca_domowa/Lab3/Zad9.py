# Zad9: Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami arytmetycznymi a drugi
# niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.

from ciagi import arytmetyczny, geometryczny

# przykład wykorzystania funkcji z modułu arytmetyczny
print("n-ty wyraz ciągu dla danych: a_1 = 15, n = 7, r = 2:")
print(arytmetyczny.n_ty_wyraz(15, 7, 2))
print("Suma n pierwszych wyrazów ciągu dla danych: a_1 = 1, a_3 = 2, n = 3")
print(arytmetyczny.suma(1, 2, 3))
print("n-ty wyraz ciągu wykorzystując sumę ciągu dla danych: s_n = 15, s_n_1 = 2")
print(arytmetyczny.n_ty_wyraz_suma(15, 2))

# przykład wykorzystania funkcji z modułu geometryczny
print("n-ty wyraz ciągu dla danych: a_1 = 1, q = 2, n = 3:")
print(geometryczny.suma(1, 2, 3))
print("Suma n pierwszych wyrazów ciągu dla danych: a_1 = 1, q = 2, n = 3")
print(geometryczny.n_ty_wyraz(1, 2, 3))
