# Zad2: Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python Comprehension zdefiniuj nową
# listę, która będzie zawierała tylko parzyste elementy

import random

lista1 = [random.randint(0, 10000) for _ in range(10)]
lista2 = [i for i in lista1 if i % 2 == 0]

print(lista1)
print(lista2)
