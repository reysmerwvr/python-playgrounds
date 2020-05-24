from operations import *

a, b, c, d = (10, 5, 0, 'Hello')

print("{} + {} = {}".format(a, b, sums(a, b)))
print("{} - {} = {}".format(b, d, diff(b, d)))
print("{} * {} = {}".format(b, b, times(b, b)))
print("{} / {} = {}".format(a, c, division(a, c)))
