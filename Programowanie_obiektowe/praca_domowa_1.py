# konwerter = Konwerter()

class Konwerter(object):

    def fahr_to_cel(self, val):
        cel = (val - 32) * 5 / 9
        return cel

    @staticmethod #<-- tworzy metodę statyczną która tworzy instancje klasy, nie musimy potem Konwerter(), tylko samo
                   # Konwerter
    def cel_to_fahr(self, val):
        fahr = val * 9 / 5 + 32
        return fahr


assert Konwerter().fahr_to_cel(32) == 0
assert Konwerter().cel_to_fahr(0) == 32
