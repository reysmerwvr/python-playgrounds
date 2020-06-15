# difference
# Returns the difference between two iterables.
#
# Use list comprehension to only keep values not contained in b


def difference(a, b):
    return [item for item in a if item not in b]


def difference_without_list_comprehension(a, b):
    difference_list = []
    for item in a:
        if item not in b:
            difference_list.append(item)
    return difference_list


difference = difference([1, 2, 3], [1, 2, 4]) # [3]
print(difference)
