import unittest
from Features.nthFibonacciValue import calculate

class TestFibonacci(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(calculate(0), 0)
        self.assertEqual(calculate(1), 1)
        self.assertEqual(calculate(2), 1)
        self.assertEqual(calculate(3), 2)
        self.assertEqual(calculate(5), 5)
        self.assertEqual(calculate(7), 13)
        self.assertEqual(calculate(10), 55)

    def test_negative_input(self):
        self.assertEqual(calculate(-1), "Enter a positive integer.")

if __name__ == '__main__':
    unittest.main()
