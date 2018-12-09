# pon = float(input("Podaj temperaturę w poniedziałek: "))
# wt = float(input("Podaj temperaturę w wtorek: "))
# sr = float(input("Podaj temperaturę w środę: "))
# czw = float(input("Podaj temperaturę w czwartek: "))
# pt = float(input("Podaj temperaturę w piątek: "))
# sob = float(input("Podaj temperaturę w sobotę: "))
# nd = float(input("Podaj temperaturę w niedzielę: "))
#
# sr_temp = (pon + wt + sr + czw + pt + sob + nd) / 7
# print(sr_temp)

# x = int(input("Podaj liczbę dni z których chcesz wyliczyć średnią temperaturę: "))
# i = 1
#
# while i <= x:
#     i = int(input("Podaj temperaturę w danym dniu: "))
#     d =
#     i += 1
#
# print()

ILE_DNI = 7

i = 1
temp = 1

while i < ILE_DNI:
    komenda = float(input(f"Podaj temperaturę w dniu {i} lub [k] by zakończyć: "))
    if komenda == 'k':
        break
    temp_i = float(komenda)
    temp += temp_i
    i += 1

print("Średnia temperatura wynosiła: ", temp/i)