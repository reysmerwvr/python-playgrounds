import math


def rectangle_area(b=None, h=None):
    if b is None or b is None:
        print("Error wrong parameters")
        return
    return b * h


def circle_area(radium):
    return (radium ** 2) * math.pi


print(circle_area(5))


def intermediate_number(a, b):
    return (a + b) / 2


print(intermediate_number(-24, 24))


def separate(list_to_separate):
    list_to_separate.sort()
    evens = []
    odds = []
    for n in list_to_separate:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)
    return evens, odds


evens, odds = separate([6, 5, 2, 1, 7])
print(evens)
print(odds)
