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
    evens_list = []
    odds_list = []
    for n in list_to_separate:
        if n % 2 == 0:
            evens_list.append(n)
        else:
            odds_list.append(n)
    return evens_list, odds_list


evens, odds = separate([6, 5, 2, 1, 7])
print(evens)
print(odds)
