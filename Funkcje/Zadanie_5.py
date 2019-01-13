def silnia(n):
    if n < 0:
        raise ValueError("Argument musi być >= 0")
    if n > 1:
        return n * silnia(n - 1)
    elif n in (0, 1):
        return 1


def dodaj(liczba):
    if liczba == 0:
        return 0
    else:
        return liczba + dodaj(liczba - 1)


print(silnia(7))
print(dodaj(2))


def test_silnia_dla_0():
    assert silnia(0) == 1


def test_silnia_dla_wieksze_od_0():
    assert silnia(5) == 120
    assert silnia(8) == 2 * 3 * 4 * 5 * 6 * 7 * 8
