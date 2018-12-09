import datetime

# current_year = datetime.datetime.now().year

# bd_year = int(input("Podaj rok urodzenia: ")
wiek = int(input("Podaj rok urodzenia: "))
print("Podaj rok urodzenia: ", wiek)

if wiek <= 2000:
    print("Jesteś pełnoletni.")
else:
    print("Nie jesteś pełnoletni.")

# if current_year - bd_year >= 18