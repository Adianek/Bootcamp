liczba_pierwsza = int(input("Podaj pierwszą liczbę: "))
liczba_druga = int(input("Podaj drugą liczbę: "))
rodz_op = input("Napisz przy użyciu znaków: +, -, *, / jaką operacje chcesz wykonać")
rodzaj_operacji = '+', '-', '*', '/'

if rodz_op == "+":
    print(liczba_pierwsza + liczba_druga)
elif rodz_op == "-":
    print(liczba_pierwsza - liczba_druga)
elif rodz_op == "*":
    print(liczba_pierwsza * liczba_druga)
else:
    print(liczba_pierwsza / liczba_druga)

