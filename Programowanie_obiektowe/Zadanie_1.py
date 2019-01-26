#Zaimplementuj klase Product przechowujaca informacje o cenie, nazwie oraz ID produktu. Zaimplementuj metode wypisujaca
# informację o produkcie na konsole

class Product:

    def __init__(self, ID, nazwa, cena):
        self.ID = ID
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"Produkt: {self.nazwa}, ID: {self.ID}, cena: {self.cena}")



product = Product(1, 'Woda', 10.99)
product.print_info()
