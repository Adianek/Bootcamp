with open("readme") as f:
    print(f.read())

with open("readme3.txt", 'w') as f:
    f.write("Ala ma kota")

with open("readme3.txt", 'a') as f:
    f.write("\nkolejna linia")
f.close()