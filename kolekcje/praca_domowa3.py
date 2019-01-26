# Napisz funkcję, która sprawdzi czy podany napis jest palindromem
# def czy_palindrom(string):
#     string = string.lower().split()
#     string = "".join(string)
#
#     lewy = 0
#     prawy = len(string) - 1
#
#     while prawy >= lewy:
#         if not string[lewy] == string[prawy]:
#             return False
#         lewy += 1
#         prawy -= 1
#
#     return True

# Krótsze rozwiązanie
def czy_palindrom(string):
    string = "".join(string.lower().split())
    return string == string[::-1]

# napis = "To jest napis"
# napis = napis.lower().split()
# "".join(napis)
assert czy_palindrom("Kobyła ma mały bok") == True
assert czy_palindrom("Zakopane na pokaz") == True
assert czy_palindrom("Ala ma kota") == False