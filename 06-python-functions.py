def greeting():
    print("Hello World")


greeting()


def draw_five_table():
    for i in range(10):
        print("5 *", i, "=", i * 5)


draw_five_table()


def test():
    print(l)


# test() Error
l = 10
test()


def test():
    num = 5
    print(num)


test()
o = 10
test()
print(o)


def test():
    return "A string returned"


test()


def test():
    return "A string returned", 20, [1, 2, 3]


c, n, cl = test()
print(c, n, cl)


def sum_nums(a, b):
    return a + b


result = sum_nums(5, 10)
print(result)


def diff(a, b):
    return a - b


print(diff(1, 2))
print(diff(b=2, a=1))


def diff(a=None, b=None):
    if a is None or b is None:
        print("Error wrong parameters")
        return
    return a - b


print(diff())
print(diff(2, 2))


def double_value(number):
    number *= 2


n = 10
double_value(n)
print(n)


def double_values(numbers):
    for i, number in enumerate(numbers):
        numbers[i] *= 2


ns = [10, 50, 100]
double_values(ns[:])
print(ns)


def indent_position(*args):
    for arg in args:
        print(arg)


indent_position(1, "Hello", [1, 2, 3])


def indent_name(**kwargs):
    for kwarg in kwargs:
        print(kwargs[kwarg])


indent_name(n=1, s="Hello", l=[1, 2, 3])


def super_function(*args, **kwargs):
    total = 0
    for arg in args:
        total += arg
    print("Total: ", total)
    for kwarg in kwargs:
        print(kwargs[kwarg])


super_function(10, 50, -1, 1.56, name="RV", age=28)


def inverse_count(num):
    num -= 1
    if num > 0:
        print(num)
        inverse_count(num)
    else:
        print("Boooom!")
    print("Number", num)


inverse_count(5)


def factorial(num):
    print("Initial Value", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("Final Value ->", num)
    return num


factorial(5)

n = int("10")
f = float("10.5")
s = "A text and a number " + str(10) + " " + str(3.14)
bin(10)
hex(10)
int('0xa', 16)
abs(6)
round(5.5)
round(5.4)
eval('2+5')
num = 10
eval('num*10 - 5')
len("Hello")
len([])
help()
