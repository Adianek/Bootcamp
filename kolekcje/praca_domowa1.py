# Zadanie 1
# def max_z_dwoch(a, b):
#     if a > b:
#         return a
#     return b
#
#
# def max_z_trzech(x, y, z):
#     return max_z_dwoch(x, max_z_dwoch(y, z))
#
#
# assert 0 == max_z_trzech(0, 0, 0)
# assert 3 == max_z_trzech(1, 2, 3)
# assert 12 == max_z_trzech(10, 2, -3)

# Zadanie 2
# isinstance(a, int)
def sumator(arg):
    total = 0
    if isinstance(arg, dict):
        arg = arg.values()
    for x in arg:
        try:
            x = int(x)
            total += x
        except ValueError:
            pass
    return total


assert sumator([1, 2, 3]) == 6
assert sumator({10, 20, 30}) == 60
assert sumator(1, 2, 'a', 3) == 6
assert sumator(1, 2, '4', 3) == 6
assert sumator({'a': 10, 1: 20, 'c': 30, 'd': 40}) == 100
