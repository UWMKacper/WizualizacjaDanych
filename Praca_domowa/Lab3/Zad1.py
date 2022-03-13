# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
# B = {1,4,16,…,4^7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}

A = [1 - x for x in range(1, 11)]
B = [4 ** x for x in range(0, 8)]
C = [x for x in B if x % 2 == 0]

print(A)
print(B)
print(C)
