from collections import defaultdict

text = input("Podaj text: ")
text = "Ala ma kota"
znaki = {

}
# znaki = defaultdict(int) -->> jezeli mam zaimportowany modul collections
for znak in text:
    # if znak in znaki:
    #     znaki[znak] += 1
    # else:
    #     znaki[znak] = 1
    # znaki[znak] += 1 w momencie gdy mamy sciagniety modul collections
    znaki[znak] =  znaki.get(znak, 0) + 1
print("Statystyka: ")
for z, c in znaki.items():
    print(f" - {z} wystąpił {c} razy.")
