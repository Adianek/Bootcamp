class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity):
        # #self.entries.append({'product': product, 'quantity': quantity})
        # add = True
        # for position in self.entries:
        #     if position [0] == product:
        #         position[1] += quantity
        #         add = False
        # if add:
        #     self.entries.append([product, quantity])
        for be in self.entries:
            if be.product == product:
                be.quantity += quantity
                break
        else:
            self.entries.append(basket_entry)

    def count_total_price(self):
        total = 0
        for e in self.entries:
            pr = e[0]
    def generate_report(self):
        report = "Produkty w koszyku: \n"
        for e in self.entries:
            report += f'- {e.product.nazwa} ({e.product.ID}), cena: {e.product.cena} x {e.quantity}\n'
        report += f"W sumie: {self.count_total_price()}"
        return report

class Product:

    def __init__(self, ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        """Wypisanie informacji o produkcie"""
        print(f"Produkt {self.nazwa}, ID: {self.ID}, cena: {self.cena} PLN.")

    def __str__(self):
        return f"<Produkt nazwa: {self.nazwa}, ID: {self.ID}>"


def test_basket_initialization():
    basket = Basket()
    assert basket.entries == []


def test_product_initialization():
    product = Product(1, "Woda", 10)
    assert product.ID == 1
    assert product.nazwa == "Woda"
    assert product.cena == 10


def test_basket_add_product():
    basket = Basket()
    product = Product(1, "Woda", 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1


def test_basket_add_product_twice():
    basket = Basket()
    product = Product(1, "Woda", 10)
    basket.add_product(product, 5)
    basket.add_product(product, 3)
    assert len(basket.entries) == 1


def test_basket_count_total_price():
    basket = Basket()
    product = Product(1, "Woda", 10)
    product = Product(2, "Ogórki", 5)
    basket.add_product(product, 5)
    basket.add_product(product, 3)
    assert basket.count_total_price() == 5 * 10 + 3 * 5

def test_basket_generate_report():
    basket = Basket()
    product = Product(1, "Woda", 10)
    basket.add_product(product, 5)
    assert basket.generate_report() == """ Produkty w koszyku:
    - Woda (1), cena: 10.0 x 5
    W sumie 50
    """
