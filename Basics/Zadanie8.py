x = int(input("Podaj szerokość opakowania w cm: "))
y = int(input("Podaj długość opakowania w cm: "))
h = int(input("Podaj wysokość opakowania w cm: "))

obj_op = x * y *h
print(f"Objętość wynosi: {obj_op}")
if obj_op > 1000:
    print("Objętość opakowania jest powyżej 1 litra.")
else:
    print("Objętość opakowania jest mniejsza od 1 litra.")
