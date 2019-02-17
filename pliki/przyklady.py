with open("readme.txt", encoding="utf-8") as f:
    print(f)
    print(f.read())

with open("readme3.txt", 'w') as f:
    f.write("Ala ma kota")


with open("readme3.txt", 'a') as f:
    f.write("\nkot ma ale")