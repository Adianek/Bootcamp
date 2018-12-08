# ctrl + alt + l ---> robi przejrzysty kod
# ctrl + / ---> zaznacza i interpreter nie czyta kodu

x = int(input("Podaj liczbę całkowitą: "))

warunek_pierwszy = (x % 2 == 0 and x % 3 == 0 and x > 10) or (x == 7)

print(warunek_pierwszy)
