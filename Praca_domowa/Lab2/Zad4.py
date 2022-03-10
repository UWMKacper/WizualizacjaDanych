# Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input

zdanie = input("Podaj zdanie: ")
zdanie_lower = zdanie.lower()
print(f"Liczba liter 'a' w podanym zdaniu: {zdanie_lower.count('a')}")
