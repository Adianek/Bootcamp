import re

pattern = re.compile("[a-z][A-Z][3][a-z][A-Z]{3}[a-z]")

with open("dane_ex3.txt") as f:
    dane = f.read()

wynik = pattern.findall(dane)
print(wynik)

