import unittest
import numberutil as numutil

class TestNumberUtil(unittest.TestCase):

    def test_total(self):
        numbers = [45, 93, 34, 71, 89, 56]
        expected_total = 388
        actual_total = numutil.total(numbers)
        self.assertEqual(expected_total, actual_total)

    def test_average(self):
        numbers = [45, 93, 34, 71, 89, 56]
        expected_average = 64.67
        actual_average = numutil.average(numbers)
        self.assertEqual(expected_average, actual_average)

    def test_minimum(self):
        numbers = [45, 93, 34, 71, 89, 56]
        expected_minimum = 34
        actual_minimum = numutil.minimum(numbers)
        self.assertEqual(expected_minimum, actual_minimum)

    def test_maximum(self):
        numbers = [45, 93, 34, 71, 89, 56]
        expected_maximum = 93
        actual_maximum = numutil.maximum(numbers)
        self.assertEqual(expected_maximum, actual_maximum)


if __name__ == '__main__':
    unittest.main()
