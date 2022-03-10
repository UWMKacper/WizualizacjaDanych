# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float.
# Następnie za pomocą użycia pętli for podnieś każdą liczbę do kwadratu.

lista = [1, 2.3, 4, 5.6, 7, 8.9, 0]
print("Lista przed zmianą: ", lista)

for i in range(len(lista)):
    lista[i] = lista[i]**2

print("Lista po podniesieniu każdego elementu do kwadratu: ", lista)
