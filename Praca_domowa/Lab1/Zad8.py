# Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na
# poszczególne wyrazy. (trzeba użyć metody split)

string = '''
"I widziałem, tak wielu stało wokół drzewa
Które, które, które, które, które wysokie jak pal
A ja bardzo, tak, tak bardzo, bardzo chciałbym wierzyć w siebie
Czy muszę stąd odchodzić, czy muszę smucić się."
'''

print('Zadany string podzielony na pojedyncze wyrazy:')
for i in string.split():
    print(i)
