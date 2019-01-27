class CashMachine:

    def __init__(self):
        self._money = []

    @property  # zmienia metode że jest wywoływana jako atrybut
    def is_available(self):
        if self._money:  # jezeli jest cos na konce wyrzuci True
            return True
        return False

    def put_money(self, bills_list):
        self._money.extend(bills_list)  # dodaje liste do listy
        self._money.sort()

    def withdraw_money(self, amount):
        money_to_withdraw = []
        for bill in sorted(self._money, reverse=True):
            if sum(money_to_withdraw) + bill <= amount:  # tu sprawdzam czy udalo sie uzbierac ile trzeba
                money_to_withdraw.append(bill)
        if sum(money_to_withdraw) != amount:
            return []
        for bill in money_to_withdraw:  #Skoro uzbieralem ile trzeba to chce to zdjac ze stanu
            self._money.remove(bill)
        return money_to_withdraw


def test_cash_machine_is_not_available():
    cash_machine = CashMachine()
    assert not cash_machine.is_available


def test_cash_machine_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available


def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.withdraw_money(150)
    assert cash_machine.withdraw_money(150) == [100, 50]
