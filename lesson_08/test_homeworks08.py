""" Оберіть від 3 до 5 різних домашніх завдань
- перетворюєте їх у функції (якщо це потрібно)
- створіть в папці файл homeworks.py куди вставте ваші функції з дз
- та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
-- імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
Код закомітьте в гіт, надайте посилання.
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""
import unittest
from homeworks import *


class TestSumTwoNumbers(unittest.TestCase):
    def test_sum_positive_numbers(self):
        """
        Testing the summation of positive numbers
        """
        num1 = 5
        num2 = 7
        expected_result = 12
        actual_result = sum_two_numbers(num1, num2)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Sum of {num1} and {num2} expected to be {expected_result}, but got {actual_result}")

    def test_sum_negative_numbers(self):
        """
        Testing the summation of negative numbers
        """
        num1 = -3
        num2 = -4
        expected_result = -7
        actual_result = sum_two_numbers(num1, num2)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Sum of {num1} and {num2} expected to be {expected_result}, but got {actual_result}")

    def test_sum_mixed_numbers(self):
        """
        Testing the summation of mixed (positive and negative) numbers
        """
        num1 = 10
        num2 = -5
        expected_result = 5
        actual_result = sum_two_numbers(num1, num2)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Sum of {num1} and {num2} expected to be {expected_result}, but got {actual_result}")


class TestReverseString(unittest.TestCase):
    def test_reverse_non_empty_string(self):
        """
        Testing the reversal of a non-empty string
        """
        test_string = "Hello, World!"
        expected_result = "!dlroW ,olleH"
        actual_result = reverse_string(test_string)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Reversed string of {test_string} expected to be {expected_result}, but got {actual_result}")

    def test_reverse_empty_string(self):
        """
        Testing the reversal of an empty string
        """
        test_string = ""
        expected_result = ""
        actual_result = reverse_string(test_string)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Reversed string of {test_string} expected to be {expected_result}, but got {actual_result}")


class TestCalculateAverage(unittest.TestCase):
    def test_average_non_empty_list(self):
        """
        Testing average calculation for a non-empty list
        """
        numbers_list = [3, 5, 7, 10, 15]
        expected_result = 8.0
        actual_result = calculate_average(numbers_list)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Average of {numbers_list} expected to be {expected_result}, but got {actual_result}")

    def test_average_empty_list(self):
        """
        Testing average calculation for an empty list
        """
        empty_list = []
        expected_result = None
        actual_result = calculate_average(empty_list)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Expected {expected_result}, but got {actual_result}")

    def test_average_single_element_list(self):
        """
        Testing average calculation for a list with a single element
        """
        single_element_list = [5]
        expected_result = 5.0
        actual_result = calculate_average(single_element_list)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Average of {single_element_list} expected to be {expected_result}, but got {actual_result}")

    def test_average_decimal_numbers(self):
        """
        Testing average calculation for a list with decimal numbers
        """
        decimal_list = [2.5, 3.5, 4.5]
        expected_result = 3.5
        actual_result = calculate_average(decimal_list)
        self.assertEqual(actual_result, expected_result,
                         msg=f"Test failed: Average of {decimal_list} expected to be {expected_result}, but got {actual_result}")

    def test_average_string_elements(self):
        """
        Testing that TypeError is raised when passing string elements to calculate_average
        """
        string_list = ["str", "qwe"]

        with self.assertRaises(TypeError, msg="Test failed: Expected TypeError for a list with string elements"):
            calculate_average(string_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)


