# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetl te zmienne

# Zmienne typu string
str_a = "text"
str_b = "nowy"

# Zmienne typu int
int_a = 5
int_b = 6

# Zmienne typu float
float_a = 5.2
float_b = 3.1

# Zmienne typu complex
complex_a = 6 + 2j
complex_b = 5 + 3j

print("Zadeklarowane zmienne:")
for var in [str_a, str_b, int_a, int_b, float_a, float_b, complex_a, complex_b]:
    print(var)
