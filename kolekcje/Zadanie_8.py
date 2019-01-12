zdanie = input("Podaj zdanie oraz wpisz jedno słowo używając nawiasów < >: ")

dlugosc = 0
licz = False
for znak in zdanie:
    if znak == '<':
        licz = True
    elif znak == '>':
        licz = False
        break # opcjonalnie
    elif licz: # zwraca nam forme True
        dlugosc += 1


print(f"liczba znaków pomiędzy <> wynosi {dlugosc}.")