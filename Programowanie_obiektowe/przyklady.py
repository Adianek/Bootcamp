# nazwy klas zaczynamy wielką literą

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        self.energy = 1100


    def nakarm(self):
        self.energy += 10


python = Animal()
python.imie = "Reksio"
python.wiek = 10
python.grupa = "Gady"

print(python.imie)
print(python.wiek)
print(python.grupa)  # Odwolanie sie do klasy


