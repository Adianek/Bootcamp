class Employee:
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stawka = stawka
        self.registered_time = 0

    def register_time(self, time):
        self.registered_time = time

    def pay_salary(self):
        worked_hours = self.registered_time
        if worked_hours > 8:
            return (self.stawka * (worked_hours - 8) * 2) + (self.stawka * worked_hours)
        else:
            return self.stawka * worked_hours

class PremiumEmployee:
