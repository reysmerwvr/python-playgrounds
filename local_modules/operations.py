def sums(a, b):
    try:
        result = float(a + b)
    except TypeError:
        print("Error: Data type not valid")
    else:
        assert isinstance(result, float)
        return result


def diff(a, b):
    try:
        result = float(a - b)
    except TypeError:
        print("Error: Data type not valid")
    else:
        assert isinstance(float(result), float)
        return result


def times(a, b):
    try:
        result = float(a * b)
    except TypeError:
        print("Error: Data type not valid")
    else:
        assert isinstance(float(result), float)
        return result


def division(a, b):
    try:
        result = float(a / b)
    except TypeError:
        print("Error: Data type not valid")
    except ZeroDivisionError:
        print("Error: Division by 0 are not allowed")
    else:
        assert isinstance(float(result), float)
        return result
