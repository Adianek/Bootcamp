napis = "abcdabcde"

for litera in napis:
    print(litera)

for i in range(len(napis)):
    print(napis[i])

print(dir(napis))

# instrukcja = input("co ma zrobic [k] by zakonczyc")
#
# if instrukcja.lower() == 'k':
#     print("Zakonczylem")

napis2 = "ala ma kota"

print(napis2.capitalize())
title = napis2.title()
print(title.istitle())
print(napis2.istitle())