# Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia

import math

# e^10
e_10 = math.pow(math.e, 10)
print(f"e^10 = {e_10}")

# 6_sqrt(ln(5 + sin^2(8))
print(f"6_sqrt(ln(5 + sin^2(8)) = {math.pow(math.log(5 + math.pow(math.sin(8), 2)), 1/6)}")

# floor(3.55)
print(f"floor(3.55) = {math.floor(3.55)}")

# ceil(4.80)
print(f"ceil(4.80) = {math.ceil(4.80)}")
