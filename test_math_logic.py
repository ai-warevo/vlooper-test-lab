import unittest
from math_logic import add

class TestMathLogic(unittest.TestCase):
    def test_add_positive_integers(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(10, 5), 15)

    def test_add_negative_integers(self):
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(1, -5), -4)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, -5), -5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=7)
        self.assertAlmostEqual(add(-1.1, 1.1), 0.0, places=7)

    def test_add_large_numbers(self):
        self.assertEqual(add(10**18, 10**18), 2 * 10**18)

if __name__ == '__main__':
    unittest.main()
