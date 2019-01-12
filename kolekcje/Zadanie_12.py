liczby = [9, 1, 6, 8, 4, 3, 2, 0]

for i in range(len(liczby)):
    indeks_minimum = i
    for j in range(i, len(liczby)):
        if liczby[j] < liczby[indeks_minimum]:
            indeks_minimum = j
    liczby[i], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[i]
print(liczby)

# print("Szukam minimum: ")
# indeks_minimum = 0
# for i in range(len(liczby)):
#     if liczby[i] < liczby[indeks_minimum]:
#         print("Znalazłem minimum")
#         print("Nowa wartość minimum to: ", liczby[i])
#         print("Nowy indeks minimum to: ", i)
#         indeks_minimum = i
# liczby[0], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[0]




assert liczby == [0, 1, 2, 3, 4, 6, 8, 9]
# def selection_sort(y):
#     for i, n in enumerate(y):
#         j, m = min(enumerate(y[i:]), key=lambda a: a[1])
#         y[j + i], y[i] = n, m
#     return y
