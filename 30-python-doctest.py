def sum_nums(a, b):
    """
    The function sum_nums(a, b) receive two parameters a and b.
    Returns sum of both numbers

    >>> sum_nums(2,2)
    4

    >>> sum_nums(0,0)
    0

    >>> sum_nums(-5,7)
    2
    """
    return a + b


def palindrome(word):
    """
    Verify if a word is a palindrome. The palindrome are words
    or phrases that you can read equally in both sides.
    Whether is palindrome returns True else False

    >>> palindrome("radar")
    True

    >>> palindrome("taco cat")
    True

    >>> palindrome("holah")
    False

    >>> palindrome("Ana")
    True

    >>> palindrome("Atar a la rata")
    True
    """
    if word.lower().replace(" ", "") == word[::-1].lower().replace(" ", ""):
        return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# python 30-python-doctest.py -v


