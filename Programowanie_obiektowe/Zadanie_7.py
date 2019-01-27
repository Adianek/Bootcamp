import pytest
import random


class Postac:
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self.ekwipunek = []

    @property
    def atak(self):
        bonusy = 0
        for przedmiot in self.ekwipunek:
            bonusy += przedmiot.bonus_do_ataku
        return self._atak + bonusy

    def otrzymaj_obrazenia(self, obrazenia):
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, uzdrowienie):
        if self.zdrowie == 0:  # Jeżeli zdrowie jest zerowe to zwraca funkcje bez leczenia
            return
        self.zdrowie += uzdrowienie
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def __str__(self):
        napis = f"""
        Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.
        EWIPUNEK:
        """
        for przedmiot in self.ekwipunek:
            # f"{przedmiot.nazwa}, {przedmiot.bonus_do_ataku} do ataku \n"
            napis += str(przedmiot)
        return napis

    def zabierz_przedmiot(self, przedmiot):
        self.ekwipunek.remove(przedmiot)

    def moc_ataku(self):
        return random.randint(self.atak // 2, self.atak)


class Przedmiot:

    def __init__(self, nazwa, bonus_do_ataku):
        self.nazwa = nazwa
        self.bonus_do_ataku = bonus_do_ataku
        """
        :param nazwa: string
        :param bonus_do_ataku: int
        """

    def __str__(self):
        napis = f"""
        Jestem {self.imie}, mam {self.atak} 
        """


def walka(atakujacy, broniacy):
    print(f"Walka {atakujacy.imie} vs {broniacy.imie}")
    print(atakujacy)
    print(broniacy)
    print("-"*40)
    moc_ataku_atakujacego =atakujacy
    broniacy.otrzymaj_obrazenia(atakujacy.moc_ataku)


def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20


def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymaj_obrazenia(200)
    assert postac.zdrowie == 0


def test_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(50)
    assert postac.zdrowie == 170


def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0


def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymaj_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200


def test_przedmiot():
    przedmiot = Przedmiot("Tulipan", 5)
    assert przedmiot.nazwa == "Tulipan"  # and przedmiot.bonus_do_ataku == 5
    assert przedmiot.bonus_do_ataku == 5


def test_postac_dodaj_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 40)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 45
    assert przedmiot in postac.ekwipunek


def test_postac_zabierz_przedmiot():
    postac = Postac("Rafał", 5, 200)
    przedmiot = Przedmiot("Rękawice grzmoty", 40)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5
    postac.dodaj_przedmiot(przedmiot)
    assert postac.atak == 45
    assert przedmiot in postac.ekwipunek
    postac.zabierz_przedmiot(przedmiot)
    assert przedmiot not in postac.ekwipunek
    assert postac.atak == 5


def test_postac_moc_ataku():
    postac = Postac("Rafał", 50, 200)
    assert postac.atak == 50
    moc_atak = postac.moc_ataku()
    assert (postac.atak // 2) <= moc_atak <= postac.atak  # // da nam wynik do calosci
