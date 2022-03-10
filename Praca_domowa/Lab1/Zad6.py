# Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się słowami
# np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzeba użyć metody count)

# fragment piosenki 'Piosenka młodych wioślarzy' zespołu Kult
string = '''
"I widziałem, tak wielu stało wokół drzewa
Które, które, które, które, które wysokie jak pal
A ja bardzo, tak, tak bardzo, bardzo chciałbym wierzyć w siebie
Czy muszę stąd odchodzić, czy muszę smucić się."
'''
print("Fragment piosenki 'Piosenka młodych wioślarzy' zespołu Kult:")
print(string)
print(f'W powyższym fragmencie słowo "tak" pojawiło się: {string.count("tak")} razy.')
