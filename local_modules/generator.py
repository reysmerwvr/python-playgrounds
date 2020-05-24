import math
import random

def read_number(start, end, message):
    while True:
        try:
            value = int(input(message))
        except:
            print('Error: Invalid number')
        else:
            if 0 <= start <= value <= end:
                break
    return value


def generator():
    numbers = read_number(1, 20, "How many numbers do you want to generate? [1-20] ")
    mode = read_number(1, 3, "How do you want to round these numbers? [1]Up [2] Down [3] Down: ")
    list_of_numbers = []
    for index in range(numbers):
        number = random.uniform(0, 101)
        if mode == 1:
            rounded_number = math.ceil(number)
            print("{} => {}".format(number, rounded_number))
        elif mode == 2:
            rounded_number = math.floor(number)
            print("{} => {}".format(number, rounded_number))
        elif mode == 3:
            rounded_number = round(number)
            print("{} => {}".format(number, rounded_number))
        list_of_numbers.append(rounded_number)
    return list_of_numbers


generator()
