import unittest
from homeworkss import calculate

class TestCalculate(unittest.TestCase):
    def test_calculate_integer1(self):
        numbers = [1, 2, 3, 4, 5]
        expected_result = 3
        result = calculate(numbers)
        self.assertEqual(result, expected_result,msg="Operation FAIL")

    def test_calculate_integer2(self):
        numbers = [1, 2, 3, 4, 5, 6]
        expected_result = 3.5
        result = calculate(numbers)
        self.assertEqual(result, expected_result,msg="Operation FAIL")

    def test_calculate_integer3(self):
        numbers = [1, 2]
        expected_result = 1.5
        result = calculate(numbers)
        self.assertEqual(result, expected_result,msg="Operation FAIL")

    def test_calculate_integer4(self):
        numbers = [1, 2, 3, 4]
        expected_result = 2.5
        result = calculate(numbers)
        self.assertEqual(result, expected_result,msg="Operation FAIL")

    def test_calculate_integer5(self):
        numbers = [1, 2, 3, 4, 5, 6, 7]
        expected_result = 7
        result = calculate(numbers)
        self.assertEqual(result, expected_result,msg="Operation FAIL")
if __name__ == '__main__':
    unittest.main(verbosity=5)