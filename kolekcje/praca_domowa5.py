import string


# Napisz funkcję, która sprawdzi, czy napis jest pangramem.

def czy_pangram(napis, alfabet=string.ascii_lowercase):
    napis = "".join(napis.lower().split())
    return len(set(napis)) == len(alfabet)


assert czy_pangram("The quick brown fox jumps over the lazy dog") == True
assert czy_pangram("ala ma kota") == False

alfabet = "abcdefghijklmnoprstuwyząęćłńóśźż"
assert czy_pangram("Pchnąć w tę łódź jeża lub ośm skrzyń fig", alfabet) == True
