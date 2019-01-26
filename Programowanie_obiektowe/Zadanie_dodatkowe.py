# Utworz kilka instancji klasy dog, Utworz tez funkcje najstarszy, ktora przyjmie dowolna ilosc instancji klasy dog i
# zwroci te, w ktorej atrybut 'age' ma najwieksza wartosc

class Dog:

    def __init__(self, nazwa, wiek):
        self.nazwa = nazwa
        self.wiek = wiek


def najstarszy(*args):
    dog_wiek = []
    for dog in args:
        dog_wiek.append([dog.wiek, dog])

    dog_wiek.sort()
    return dog_wiek[-1][1]

# x = [[10, 1], [9, 2], [7, 4]]
# x.sort()
# print(x)

rex = Dog("Rex", 10)
brutus = Dog("Brutus", 15)

print(najstarszy(rex, brutus).nazwa)
