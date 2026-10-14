import unittest

from math_logic import add, pow, sqrt


class TestMathLogic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2.0)
        self.assertEqual(sqrt(9), 3.0)
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=7)
        self.assertEqual(sqrt(0), 0.0)
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_pow(self):
        self.assertEqual(pow(2, 3), 8.0)
        self.assertEqual(pow(5, 0), 1.0)
        self.assertEqual(pow(9, 0.5), 3.0)
        with self.assertRaises(ValueError):
            pow(-1, 0.5)
        with self.assertRaises(ValueError):
            pow(0, -1)

if __name__ == '__main__':
    unittest.main()
