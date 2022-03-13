# wzory dla ciągów geometrycznych

def n_ty_wyraz(a, q, n, k=1):
    return a * q ** (n - k)


def suma(a, q, n):
    if q == 1:
        return a * n
    else:
        return a * ((1 - q ** n) / (1 - q))
