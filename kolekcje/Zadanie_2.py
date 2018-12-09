lista = []
i = 0
while i <= 10:
    liczba = input("Podaj liczbę lub k by zakończyć: ")
    if liczba == 'k':
        break
    liczba = int(liczba)
    lista.append(liczba)
    i += 1

print("Średnia wynosi: ", sum(lista)/len(lista))

