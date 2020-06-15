# https://docs.python.org/2/library/itertools.html#itertools.chain
# https://www.python.org/dev/peps/pep-0255/
# https://codeburst.io/understanding-generators-in-es6-javascript-with-examples-6728834016d5#:~:text=Generators%20are%20a%20special%20class,%E2%80%8Ba%20series%20of%20values.

list1 = [number for number in [0, 1, 2, 3, 4, 5] if number % 2 == 0]
print(list1)
list1 = [number for number in range(0, 6) if number % 2 == 0]
print(list1)


#######################################################################################################################


def even(n):
    for number in range(n + 1):
        if number % 2 == 0:
            yield number


even(10)
for number in even(10):
    print(number)

list1 = [number for number in even(10)]
print(list1)

#######################################################################################################################

even = even(3)
next(even)
next(even)
# next(even)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-10-771f3ce83b3e> in <module>
# ----> 1 next(even)
#
# StopIteration:

#######################################################################################################################

list1 = [1, 2, 3, 4, 5]
iterable_list = iter(list1)
iterable_list
next(iterable_list)
next(iterable_list)
next(iterable_list)
next(iterable_list)

#######################################################################################################################

string1 = "Hello"
iterable_string = iter(string1)
iterable_string
next(iterable_string)
next(iterable_string)
next(iterable_string)
next(iterable_string)


#######################################################################################################################

def natural_numbers():
    num = 1
    while True:
        yield num
        num += 1


numbers = natural_numbers()
print(next(numbers))
print(next(numbers))


#######################################################################################################################


def power_series(number, power):
    base = number
    while True:
        yield base ** power
        base += 1


#######################################################################################################################


def take(n, iterable):
    index = 0
    for iter_value in iterable:
        if index >= n:
            return
        index += 1
        yield iter_value


#######################################################################################################################

values = take(3, iter(['a', 'b', 'c', 'd', 'e']))

for value in values:
    print(value)
# With List Comprehension
list1 = [value for value in take(3, iter(['a', 'b', 'c', 'd', 'e']))]
print(list1)

list1 = [value for value in take(4, natural_numbers())]
print(list1)

list1 = [value for value in take(4, natural_numbers())]
print(list1)

list1 = [value for value in take(5, power_series(3, 2))]
print(list1)

#######################################################################################################################


