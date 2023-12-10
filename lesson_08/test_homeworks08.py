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
from test_functions import my_substr
from test_functions import sum_of_two_numbers
from test_functions import square_of_even_numbers


class TestMySubstr(unittest.TestCase):

    def test_positive_slice(self):

        """"Positive slice test """
        result = my_substr("Hello, World!", 5)
        self.assertEqual(result, "Hello")

    def test_zero_slice(self):

        """Test if slice = 0"""
        result = my_substr("Hello, World!", 0)
        self.assertEqual(result, "")

        """test with minus slice"""
    def test_negative_slice(self):
        result = my_substr("Hello, World!", -5)
        self.assertEqual(result, "")

        """Test negative when slice none"""
    def test_negative_case_none_slice(self):
        with self.assertRaises(TypeError):
            my_substr("Hello, World!", None)

        """Test negative when slice more them length string"""
    def test_negative_case_long_slice(self):
        with self.assertRaises(IndexError):
            my_substr("Hello, World!", 15)


class TestSumOfTwoNumbers(unittest.TestCase):

    """Test on int numbers"""
    def test_positive_sum_of_integers(self):
        result = sum_of_two_numbers(3, 7)
        self.assertEqual(result, "Сума двох чисел 3 та 7 дорівнює: 10")

    """Test of float numbers"""
    def test_positive_sum_of_floats(self):
        result = sum_of_two_numbers(2.5, 1.5)
        self.assertEqual(result, "Сума двох чисел 2.5 та 1.5 дорівнює: 4.0")

    """Test of int with float numbers"""
    def test_positive_sum_of_mixed_types(self):
        result = sum_of_two_numbers(5, 2.5)
        self.assertEqual(result, "Сума двох чисел 5 та 2.5 дорівнює: 7.5")


class TestsSquareOfEvensNumbers(unittest.TestCase):

    """Test with empty list"""
    def test_negative_with_empty_list(self):
        result = square_of_even_numbers([])
        self.assertEqual(result, [], "Expected an empty list for an empty input")
    """Test list with NOT even numbers"""
    def test_negative_no_even_numbers(self):
        result = square_of_even_numbers([1, 3, 5])
        self.assertEqual(result, [], "Expected an empty list for no even numbers" )

    """Test list of even numbers"""
    def test_square_of_even_numbers(self):
        result = square_of_even_numbers([2, 4, 6, 8])
        self.assertEqual(result, [4, 16, 36, 64], "Expected squared even numbers")

    """Test with mixed numbers in the list"""
    def test_mixed_numbers(self):
        result = square_of_even_numbers([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, [4, 16, 36], "Expected squared even numbers from the mixed list")


if __name__ == '__main__':
    unittest.main(verbosity=2)
