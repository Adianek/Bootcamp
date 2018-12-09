lista = [1, 2, 3, -1, -2, -3]
dodatnie = 0
ujemne = 0
# for liczba in lista:
#     if liczba > 0:
#         dodatnie += 1
#     if liczba < 0:
#         ujemne += 1
#
# print("Ilość liczb dodatnich:", dodatnie)
# print("Ilość liczb ujemnych:", ujemne)

dodatnie = len([x for x in lista if x > 0])
ujemne = len([x for x in lista if x < 0])

print(dodatnie)
print(ujemne)