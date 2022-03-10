# Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne

print("\nAplikacja kalkulator\n")
print("W kalkulatorze można wykorzysać następujące działania arytmetyczne: +, -, /, *, **, //, %")
print("Przykładowe działanie: do obliczenia sumy 6 i 7 należy wprowadzić wartość: 6+7, a następnie należy wcisnąć \
klawisz 'Enter'.")
print("Aby zakończyć działanie kalkuatora należy wcisnąć klawisz 'Enter' bez podawania wartości do obliczenia.")

while True:
    a = input("\nPodaj działanie: ")
    if a:
        try:
            x = eval(a)
            print(f"Wynik obliczeń: {x}")
        except Exception as e:
            print(f"Pojawił się błąd: {e}")
    else:
        print("\nDo widzenia!")
        break
