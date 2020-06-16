import unittest


def double(a): return a * 2


class TestFixture(unittest.TestCase):
    def setUp(self) -> None:
        print("Preparing the context")
        self.numbers = [1, 2, 3, 4, 5]

    def test_double(self):
        print("Executing Test")
        r = [double(n) for n in self.numbers]
        self.assertEqual(r, [2, 4, 6, 8, 10])

    def tearDown(self) -> None:
        print("Destroying the context")
        del self.numbers


if __name__ == "__main__":
    unittest.main()

# python 31-python-unittest-1.py -v
