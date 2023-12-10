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
from my_methods import MyMethods
from unittest.mock import patch

class UntTests(unittest.TestCase):

    def test_addit_positive_num(self):
        """
        Method: addit
        Test is aimed to check addition
        of positive numbers
        """
        input_a = 1
        input_b = 5
        expected = 6
        actual_result = MyMethods.addit(input_a, input_b)
        self.assertEqual(expected, actual_result)

    def test_addit_negative_num(self):
        """
        Method: addit
        Test is aimed to check addition
        of negative numbers
        """
        input_a = -3
        input_b = -9
        expected = -12
        actual_result = MyMethods.addit(input_a, input_b)
        self.assertEqual(expected, actual_result)

    def test_addit_negative_positive_num(self):
        """
        Method: addit
        Test is aimed to check addition
        of negative and positive numbers
        """
        input_a = -3
        input_b = 6
        expected = 3
        actual_result = MyMethods.addit(input_a, input_b)
        self.assertEqual(expected, actual_result)

    def  test_list_avg_positive_negative_elements(self):
        """
        Method: list_avg
        Test is aimed to check arithmetic
        mean of positive and negative numbers into the list
        """
        list_of_numbers = [1, 2, -3, 4, -5]
        expected = -0.2
        actual = MyMethods.list_avg(list_of_numbers)
        self.assertEqual(expected, actual)

    def  test_list_avg_zero_elements(self):
        """
        Method: list_avg
        Test is aimed to check arithmetic
        mean of zero into the list
        """
        list_of_numbers = [0, 0, 0, 0]
        expected = 0
        actual = MyMethods.list_avg(list_of_numbers)
        self.assertEqual(expected, actual)

    def  test_list_avg_one_element(self):
        """
        Method: list_avg
        Test is aimed to check arithmetic
        mean of one element into the list
        """
        list_of_numbers = [222]
        expected = 222
        actual = MyMethods.list_avg(list_of_numbers)
        self.assertEqual(expected, actual)

    def test_revers_string_letters_numbers(self):
        """
        Method: revers_string
        Test is aimed to check reversing line
        with letters and numbers
        """
        normal_string = "1a2b3c4d5"
        expected = "5d4c3b2a1"
        actual = MyMethods.revers_string(normal_string)
        self.assertEqual(expected, actual)

    def test_revers_string_spaces(self):
        """
        Method: revers_string
        Test is aimed to check reversing line
        with letters and numbers
        """
        normal_string = " abc   "
        expected = "   cba "
        actual = MyMethods.revers_string(normal_string)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['01689']) # Знайшов рішення в інтернете - емулюує ввод користувача (я паятаю, що ви казали, що це не дуже влучна функція, бо потребує рекурсії)
    def test_sum_of_input_digits_positive(self, user_input):
        """
        Method: sum_of_input_digits
        Test is aimed to check that each
        entered digit added
        """
        expected = 24
        actual = MyMethods.sum_of_input_digits()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['abc '])
    def test_sum_of_input_not_digit_message(self, user_input):
        """
        Method: sum_of_input_digits
        Test is aimed to check the message "Enter digit!!!" is called
        when entered not a numbers
        """
        expected = "Enter digit!!!"
        actual = MyMethods.sum_of_input_digits()
        self.assertEqual(actual, expected)

    @patch('builtins.input', side_effect=['0'])
    def test_sum_of_input_zero_message(self, user_input):
        """
        Method: sum_of_input_digits
        Test is aimed to check the message "Enter digit!!!" is called
        when entered not a numbers
        """
        expected = "Digit must be above 0!"
        actual = MyMethods.sum_of_input_digits()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()