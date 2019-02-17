import tkinter
from tkinter import messagebox


def policz_spalanie():
    d = int(dystans.get())
    c = float(cena.get())
    s = float(spalanie.get())

    w = d * s * c * 0.01
    wynik.configure()


root = tkinter.Tk()

dystans_label = tkinter.Label(master=root, text="Dystans: ")
dystans_label.grid(row=0, column=0)
dystans = tkinter.Entry(master=root)
dystans.grid(row=0, column=1)

spalanie_label = tkinter.Label(master=root, text="Dystans: ")
spalanie_label.grid(row=1, column=0)
spalanie = tkinter.Entry(master=root)
spalanie.grid(row=1, column=0)

cena_label = tkinter.Label(master=root, text="Dystans: ")
cena_label.grid(row=2, column=0)
cena = tkinter.Entry(master=root)
cena.grid(row=2, column=1)

policy = tkinter.Button(master=root, text="")

root.mainloop()

# def srednia_spalania():
#     print("Naciśnięto przycisk")
#     try:
#         a = float(input(a_entry.get()))
#         b = float(input(b_entry.get()))
#         wynik = (a/b) * 100
#         wynik_label.configure(text=f"Wynik: {wynik}")
#     except ValueError:
#         messagebox.showerror("Błędne dane", "Popraw dane - powinny być liczbami")
#
#
#
#
# root = tkinter.Tk()
#
# a_label = tkinter.Label(master=root, text="cena paliwa")
# a_label.grid(row=0, column=0)
# a_entry = tkinter.Entry(master=root)
# a_entry.grid(row=0,column=1)
#
# b_label = tkinter.Label(master=root, text="spalanie samochodu")
# b_label.grid(row=1, column=0)
# b_entry = tkinter.Entry(master=root)
# b_entry.grid(row=1, column=1)
#
# button = tkinter.Button(master=root, text="Sum", command=srednia_spalania)
# button.grid(row=2, column=1)
#
# wynik_label = tkinter.Label(master=root, text=" - ")
# wynik_label.grid(row=3, column=1)
#
# root.mainloop()  # standardowe okno
