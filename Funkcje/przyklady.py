# liczby = [1, 2, 3, 4]
# liczby2 = [5, 6, 7, 8]
#
#
# # for i, l in enumerate(liczby):
# #     print(f'Indeks={i}, wartość={l}')
# # for i, l in enumerate(liczby2):
# #     print(f'Indeks={i}, wartość={l}')
#
#
# def drukuj(lista):
#     for i, l in enumerate(lista):
#         print(f"Indeks={i}, wartość={l}")
#
#
# drukuj(liczby)
#
#
# def dodaj_a_b(a, b):


# def potega(podstawa, wykladnik=2):
#     return podstawa ** wykladnik
#
#
# print(potega(4, 2))

# def wykonaj_operacje(operacja, *args):
#     print(args)
#     print(type(args))
#     return operacja(args)
#
#
# print(wykonaj_operacje(min, 10, 20, 30, 40, 50))
# print(wykonaj_operacje(sum, 10, 20, 30, 50, 60))
# print(wykonaj_operacje(max, 10, 20, 30, 40, 50))

def napisy(*args):
    return "\n".join(args)


print("-" * 40)
print(napisy("a", "b"))

"""
Napisz funkcję, która przyjmie dowolną liczbę napisów,
1. zwróci te napisy połączone znakiem nowej linii

>>> napisy("a", "b")
a
b

>>> napisy("a", "b", "d")
a
b
d


"""
