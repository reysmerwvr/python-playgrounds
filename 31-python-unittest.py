import unittest


def double(a): return a * 2


def sum_args(a, b): return a + b


def is_even(a): return True if a % 2 == 0 else False


class FunctionTests(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(10), 20)
        self.assertEqual(double('AB'), 'ABAB')

    def test_sum_args(self):
        self.assertEqual(sum_args(-15, 15), 0)
        self.assertEqual(sum_args('AB', 'CD'), 'ABCD')

    def test_is_even(self):
        self.assertEqual(is_even(68), True)
        self.assertEqual(is_even(11), False)

    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

    def test_split(self):
        string = "Hello World"
        self.assertEqual(string.split(" "), ["Hello", "World"])

    # def test(self):
    # pass
    # raise AssertionError()
    # 1/0


if __name__ == "__main__":
    unittest.main()

# python 31-python-unittest.py -v
