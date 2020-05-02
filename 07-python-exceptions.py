try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error! Not allowed division by zero")

try:
    list1 = [1, 2, 3, 4, 5]
    list1[10]
except IndexError:
    print("Error! Trying to access undefined index. List Length: ", len(list1))

try:
    colors = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
    colors['white']
except KeyError:
    print("Error! Trying to access to undefined property")

try:
    result = 15 + "20"
except TypeError:
    print("Error! Trying to operate different type values")

elements = [1, 5, -2]


def add_one_time(list_1, element):
    try:
        if element in list_1:
            raise ValueError
        else:
            list_1.append(element)
    except ValueError:
        print("Error: Trying to add duplicated value to list -> {}".format(element))


add_one_time(elements, 10)
add_one_time(elements, -2)
add_one_time(elements, "Hello")
print(elements)
