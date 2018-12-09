# cena za kilogram produktu
cena = 10.0
# ile towaru zostało zakupionego
waga = int(input("Podaj wagę jaką chcesz zakupić: "))
# ile zaplacimy za towar
naleznosc = cena * waga

# print("Cena za kilogram: ", cena)
# print("Waga: " + str(waga))
# print("Za zakupiony towar zapłacisz: ",naleznosc, " PLN.")

info = f"""
Cena za kg: {cena}
Waga: {waga}
Należność: {naleznosc}
"""
print(info)