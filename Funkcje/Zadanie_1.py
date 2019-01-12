def czy_jest_pierwsza(a):
    if (a % 2 == 1) or (a == 2):
        print("Liczba jest liczbą pierwszą.")
    else:
        print("Liczba nie jest liczbą pierwszą.")
        return True
czy_jest_pierwsza(253)

# assert czy_jest_pierwsza(17) == True
# assert not czy_jest_pierwsza(10)