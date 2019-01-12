liczba_parzystych = set(range(0, 100, 2))
liczby = set({})
while True:
    liczba = input("Podaj liczby całkowite lub [k] by zakończyć: ")
    if liczba == 'k':
        break
    else:
        liczby.add(int(liczba))

print(liczby)
print("Liczb unikalnych jest: ", len(liczby))
print("Z tego parzystych jest: ", len(liczby & liczba_parzystych))
