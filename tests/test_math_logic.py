import unittest
from math_logic import add, sqrt, pow

class TestMathLogic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2.0)
        self.assertEqual(sqrt(0), 0.0)
        self.assertAlmostEqual(sqrt(2), 1.41421356, places=7)

    def test_pow(self):
        self.assertEqual(pow(2, 3), 8.0)
        self.assertEqual(pow(5, 0), 1.0)
        self.assertAlmostEqual(pow(2, -1), 0.5, places=7)

if __name__ == '__main__':
    unittest.main()
