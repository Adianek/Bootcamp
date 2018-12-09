miasto_A = input("Podaj nazwę miasta z którego wyjeżdzasz: ")
miasto_B = input("Podaj nazwę miasta do którego zmierzasz: ")
# int(input(f"Dystans{miasto_A} {miasto_B}")) można też tak
dystans_A_B = int(input("Jaki jest dystans między " + miasto_A + " ,a " + miasto_B +": "))
cena_paliwa = float(input("Jaka jest cena paliwa: "))
spalanie = float(input("Podaj średnie spalanie twojego samochodu: "))
# wyliczenie kosztu przejazdu
koszt_przejazdu = dystans_A_B * spalanie * cena_paliwa / 100
# print(f"koszt_przejazdu {miasto_A} - {miasto_B} to {koszt} PLN")
print("Koszt przejazdu między " + miasto_A + "-" + miasto_B + " to", koszt_przejazdu)