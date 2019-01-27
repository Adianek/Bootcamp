class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Cześć jeestem {self.imie} {self.nazwisko}")


class Pracownik(Osoba):

    def pracuj(self):
        print("Pracuję ...")

    def __init__(self, imie, nazwisko, stanowisko):
        super().__init__(imie, nazwisko)
        self.stanowisko = stanowisko

        # self.imie = imie
        # self.nazwisko = nazwisko
        # self.stanowisko = stanowisko

    # def przedstaw_sie(self):
    #     print(f"Cześć jeestem {self.imie} {self.nazwisko}")


osoba = Osoba("Adam", "Słodowy")
osoba.przedstaw_sie()

pracownik = Pracownik("Rafał", "Korzeniewski")
pracownik.prze