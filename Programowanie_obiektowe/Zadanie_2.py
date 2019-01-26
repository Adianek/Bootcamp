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
# PROGRAM NIE DZIAŁA POPRAWNIE ZA DUZO DODAJE - DO ZMIANY

employee = Employee("Jan", "Kowalski", 100)
employee.register_time(10)
print(employee.pay_salary())

# def test_pay_salary_without_register_time():
#     employee = Employee("Jan", "Kowalski", "100")
#     assert employee.pay_salary() == 0
#
#
# def test_employee_initialization():
#     employee = Employee("Jan", "Kowalski", "100")
#     employee.register_time(5)
#     assert employee.pay_salary() == 500
#     assert employee.pay_salary() == 0
#
#
# def test_employee_over_hours():
#     employee = Employee("Jan", "Kowalski", "100")
#     employee.register_time(10)
#     assert employee.pay_salary() == 800 + 400
#     assert employee.pay_salary() == 0
