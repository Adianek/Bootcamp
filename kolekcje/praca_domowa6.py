# Napisz funkcję, która sprawdzi, czy zadana liczna jest doskonała

def liczba_doskonala(liczba):
    total = 0
    for a in range(1, liczba):
        if liczba % a == 0:
            total += a

    return total == liczba

"""
Pomysły na optymalizację:
1. sprawdzenie dzielenia tylko do ~ n/2
2. jeśli coś nie jest podzielne przez 2 to nie będzie też przez żadną liczbę parzystą
3. nie znaleziono dotąd żadnej liczby , która jest nieparzysta.
"""


assert liczba_doskonala(6) == True
assert liczba_doskonala(7) == False
assert liczba_doskonala(28) == True
assert liczba_doskonala(496) == True
