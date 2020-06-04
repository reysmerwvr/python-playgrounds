# average :information_source: Already implemented via statistics.mean. statistics.mean takes an array as an argument
# whereas this function takes variadic arguments.
#
# Returns the average of two or more numbers.
#
# Takes the sum of all the args and divides it by len(args). The second argument 0.0 in sum is to handle floating
# point division in python3.

def average(*args):
    return sum(args, 0.0) / len(args)


print(average(*[1, 2, 3]))  # 2.0
print(average(1, 2, 3))  # 2.0
