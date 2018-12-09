x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if (x < 0 or y < 0) or (x > 100 or y > 100):
    print("Gracz jest poza planszą")
elif x <= 10 and y <= 10 and x >= 0 and y >= 0:
    print("Gracz znajduje się w lewej dolnej krawędzi")
elif x >= 90 and y >= 90 and x <= 100 and y <= 100:
    print("Gracz znajduje się w prawej górnej krawędzi")
elif x <= 10 and y >= 90 and x >= 0 and y >= 0 and x <= 100 and y <= 100:
    print("Gracz znajduje się w lewej górnej krawędzi")
elif x >= 90 and y <= 90 and x <= 100 and y <= 100:
    print("Gracz znajduje się w prawej dolnej krawędzi")
elif x <= 10 and y > 10 and y < 90 and x >= 0:
    print("Gracz znajduje się w lewej krawędzi")
elif x >= 90 and y > 10 and y < 90 and x <= 100:
    print("Gracz znajduje się w prawej krawędzi")
elif x > 10 and x < 90 and y >= 0 and y <= 10:
    print("Gracz znajduje się w dolnej krawędzi")
elif x > 90 and x <= 100 and y > 90 and y <= 100:
    print("Gracz znajduje się w górnej krawędzi")
else:
    print("Gracz znajduje się w centrum")