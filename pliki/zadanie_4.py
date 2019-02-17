import json

#
#
# pracownik = {}
#
#
#
# wybor = input("Jeśli chcesz dodać pracownika - d, jeśli wypisać - w, jeśli zakończyć - z ")
# if wybor == 'z':
#     print("W takim razie Dziękuję.")
#     quit()
# elif wybor == 'd':
#     imie = input("Podaj imię: ")
#     nazwisko = input("Podaj nazwisko: ")
#     rok_urodzenia = int(input("Podaj rok urodzenia: "))
#     pensja = int(input("Podaj wynagrodzenie"))
#     pracownik['imie'] = imie
#     pracownik['nazwisko'] = nazwisko
#     pracownik['rok_urodzenia'] = rok_urodzenia
#     pracownik['pensja'] = pensja
#
#
#
#
# json_list = json.dumps(pracownik)
# print(pracownik)

# Rafala rozwiazanie
try:
    with open("employees.json") as fp:
        pracownicy = json.load(fp)
except FileNotFoundError:
    pracownicy = []


def dodaj_pracownika(pracownicy):
    imie = input("Podaj imie: ")
    nawzwisko = input("Podaj nazwisko: ")
    rok_urodzenia = input("Podaj rok urodzenia: ")
    pensja = input("Pensja: ")

    pracownik = {
        "imie": imie,
        "nazwisko": nawzwisko,
        "rok_urodzenia": rok_urodzenia,
        "pensja": pensja
    }
    pracownicy.append(pracownik)

    with open("employees.json", 'w') as fp:
        json.dump(pracownicy, fp)


def wypisz_pracownika():
    print("Pracownicy: ")
    for nr, pracownik in enumerate(pracownicy):
        print(f"- [{nr}] {pracownik['imie']} {pracownik['nazwisko']} - rok: {pracownik['rok_urodzenia']},"
              f"pensja: {pracownik['pensja']} PLN")


wybor = input("Co chcesz zrobić? [d - dodaj, w - wypisz]: ")

if wybor == 'd':
    dodaj_pracownika(pracownicy)
elif wybor == 'w':
    wypisz_pracownika(pracownicy)
