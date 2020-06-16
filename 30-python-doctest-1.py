def double(list_to_double):
    """Double each element in a list
    >>> l = [1, 2, 3, 4, 5]
    >>> double(l)
    [2, 4, 6, 8, 10]

    >>> l = []
    >>> for value in range(10):
    ...     l.append(value)
    >>> double(l)
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    return [n*2 for n in list_to_double]


def sum_arguments(a, b):
    """
    The function sum_nums(a, b) receive two parameters a and b.
    Returns sum of both

    Numbers:
    >>> sum_arguments(2,2)
    4

    >>> sum_arguments(-5,7)
    2

    Strings:
    >>> sum_arguments('aa', 'bb')
    'aabb'

    List:
    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> sum_arguments(a, b)
    [1, 2, 3, 4, 5, 6]

    Different types:
    >>> sum_arguments(10, "Hello")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'

    """
    return a + b


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# python 30-python-doctest-1.py -v
